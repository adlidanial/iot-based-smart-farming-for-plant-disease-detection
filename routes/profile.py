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

class Profile:
    @routes.route('/profile', methods = ['GET', 'POST'])
    def profile():
        successProfile = False
        failPassProfile = False

        cursor = mysql.get_db().cursor()
        if session['roles'] == 1:
            cursor.execute('SELECT * FROM farmer WHERE PK_ID = %s', (session['id']))
            data = cursor.fetchall()
        else:
            cursor.execute('SELECT * FROM expertadvisor WHERE PK_ID = %s', (session['id']))
            data = cursor.fetchall()
        
        for row in data:
            fullname = row[1]
            email = row[2]
            username = row[3]

        if request.method == 'POST':
            if(request.form['btnSubmit'] == "profile"):
                fullname = request.form['fullname']
                email = request.form['email']
                username = request.form['username']

                cursor = mysql.get_db().cursor()
                if session['roles'] == 1:
                    cursor.execute('UPDATE farmer SET FULL_NAME = %s, EMAIL = %s, USERNAME = %s WHERE PK_ID = %s', (fullname, email, username, session['id']))
                else:
                    cursor.execute('UPDATE expertadvisor SET FULL_NAME = %s, EMAIL = %s, USERNAME = %s WHERE PK_ID = %s', (fullname, email, username, session['id']))
                cursor.connection.commit()
                successProfile = True
                session['fullname'] = fullname
            elif(request.form['btnSubmit'] == "pass"):
                print("sini")
                password = request.form['pass']
                repass = request.form['repass']

                if(password == repass):
                    cursor = mysql.get_db().cursor()
                    if session['roles'] == 1:
                        cursor.execute('UPDATE farmer SET PASSWORD = %s WHERE PK_ID = %s', (password, session['id']))
                    else:
                        cursor.execute('UPDATE expertadvisor SET PASSWORD = %s WHERE PK_ID = %s', (password, session['id']))
                    cursor.connection.commit()
                    successProfile = True
                else:
                    failPassProfile = True

        return render_template('profile.html', name = fullname, email = email, username = username, successProfile = successProfile, failPassProfile = failPassProfile)
