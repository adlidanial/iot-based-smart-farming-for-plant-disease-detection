from flask import (render_template, Flask, request, redirect, url_for, session)
from flaskext.mysql import MySQL
from . import routes
from routes.connect import HOST, USER, PASSWORD, DB

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = HOST
app.config['MYSQL_DATABASE_USER'] = USER
app.config['MYSQL_DATABASE_PASSWORD'] = PASSWORD
app.config['MYSQL_DATABASE_DB'] = DB

mysql = MySQL(app)

class ListPlantDisease:
    @routes.route('/listplantdisease')
    def listplantdisease():
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM PLANTDISEASE')
        dataplantdisease = cursor.fetchall()

        return render_template('listplantdisease.html', data = dataplantdisease)

    