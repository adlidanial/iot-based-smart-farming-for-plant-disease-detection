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

class AddExpertAdvisor:
    def __init__(self, fullname, email, username, password):
        self.__fullname = fullname
        self.__email = email
        self.__username = username
        self.__password = password
    
    def verifyAdd(self):
        erremail = False
        errusername = False        
        
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM expertadvisor WHERE USERNAME = %s AND EMAIL = %s', (self.__username, self.__email))
        expadv = cursor.fetchall()
        if expadv:
            if expadv[2] == self.__email:
                erremail = True
            if expadv[3] == self.__username:
                errusername = True            

        return erremail, errusername

    @routes.route('/addexpertadvisor', methods = ['GET', 'POST'])
    def addexpertadvisor():
        msgPassword = False
        msgSuccess = False
        msgErr = False

        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            repassword = request.form['repassword']

            if(name != '' and email != '' and username != '' and password != '' and repassword != ''):
                if password != repassword:
                    msgPassword = True
                    return render_template('addexpertadvisor.html', msgPassword = msgPassword)
                else:
                    val = AddExpertAdvisor(name, email, username, password)
                    erremail, errusername = val.verifyAdd()

                    if(not(erremail) and not(errusername)):
                        cursor = mysql.get_db().cursor()
                        cursor.execute('INSERT INTO expertadvisor (FK_ID_ADMIN, FULL_NAME, EMAIL, USERNAME, PASSWORD) VALUES (%s, %s, %s, %s, %s)', (session['id'], name, email, username, password))
                        cursor.connection.commit()
                        msgSuccess = True
                        return render_template('addexpertadvisor.html', msgSuccess = msgSuccess)
                    else:
                        msgErr = True
                        return render_template('addexpertadvisor.html', msgErr = msgErr)
        return render_template('addexpertadvisor.html')