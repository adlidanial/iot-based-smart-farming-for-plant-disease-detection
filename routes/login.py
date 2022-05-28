from flask import (render_template, Flask, request, redirect, url_for, session)
from flaskext.mysql import MySQL
from . import routes
from routes.connect import HOST, USER, PASSWORD, DB
from passlib.hash import sha256_crypt

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = HOST
app.config['MYSQL_DATABASE_USER'] = USER
app.config['MYSQL_DATABASE_PASSWORD'] = PASSWORD
app.config['MYSQL_DATABASE_DB'] = DB


mysql = MySQL(app)

class Login:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def verifyLogin(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM farmer WHERE USERNAME = %s', (self.__username))
        farmer = cursor.fetchall()

        cursor.execute('SELECT * FROM admin WHERE USERNAME = %s', (self.__username))
        admin = cursor.fetchall()

        cursor.execute('SELECT * FROM expertadvisor WHERE USERNAME = %s', (self.__username))
        expadv = cursor.fetchall()

        if farmer:
            data = farmer
            for row in data:
                hash_password = row[4]

            if sha256_crypt.verify(self.__password, hash_password):
                result = 1
            else:
                result = 0
                data = 0
        elif admin:
            data = admin
            for row in data:
                hash_password = row[4]

            if sha256_crypt.verify(self.__password, hash_password):
                result = 2
            else:
                result = 0
                data = 0
        elif expadv:
            data = expadv
            for row in data:
                hash_password = row[5]
            
            if sha256_crypt.verify(self.__password, hash_password):
                result = 3
            else:
                result = 0
                data = 0
        else:
            result = 0
            data = 0
            
        return result, data

    @routes.route('/login', methods = ['GET', 'POST'])
    def login():
        errmsg = ''
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            val = Login(username, password)
            result, data = val.verifyLogin()
            if result != 0:
                for row in data:
                    session['id'] = row[0]
                    if result == 3:
                        session['fullname'] = row[2]
                    else:
                        session['fullname'] = row[1]
                    session['username'] = row[3]
                    session['roles'] = result
                errmsg = False
                if result == 2:
                    return redirect(url_for('.dashboard'))
                else:
                    return redirect(url_for('.index'))
            else:
                errmsg = True


        return render_template('login.html', msg = errmsg)
