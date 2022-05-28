import os
from flask import (render_template, Flask, request, redirect, url_for, session)
from flaskext.mysql import MySQL
from routes.connect import HOST, USER, PASSWORD, DB
from werkzeug.utils import secure_filename
from . import routes
from datetime import datetime


app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = HOST
app.config['MYSQL_DATABASE_USER'] = USER
app.config['MYSQL_DATABASE_PASSWORD'] = PASSWORD
app.config['MYSQL_DATABASE_DB'] = DB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = 'static/uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mysql = MySQL(app)

class CropDisease:
    # function to check the extension of image
    def allowed_file(self, filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @routes.route('/crop-disease', methods = ['GET', 'POST'])
    def cropdisease():
        errmsg = False
        ob = CropDisease()
        if request.method == 'POST':
            f = request.files['uploadImage']  # assign the file image from upload file
            if f.filename == "": # if name of file is null/empty
                errmsg = True
            elif f and ob.allowed_file(f.filename): 
                today = datetime.today() # get date and time today
                d = today.strftime("%d%m%Y%H%M%S")

                special_char = '@!#$%^&*()<>?/\|}{~:;[]' # initializing special characters
                for i in special_char:  # using replace () to remove special characters
                    f.filename = f.filename.replace(i, '')
                newfilename = f.filename.replace(" ", "_")
                strfilename = d + "_" + newfilename

                strfilename = secure_filename(strfilename) # store image into folder uploads
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], strfilename))
                session["urlimage"] = strfilename # store path image into session

                cursor = mysql.get_db().cursor() # connect database to insert
                cursor.execute('INSERT INTO loghistory (FK_ID_FARMER, URL_IMAGE, DATE_CREATED) VALUES (%s, %s, %s)', 
                (session["id"], session["urlimage"], datetime.now()))
                cursor.connection.commit()
                session["lastid_loghistory"] = cursor.lastrowid

                return redirect(url_for('.result'))

        return render_template('crop-disease.html', msg = errmsg)