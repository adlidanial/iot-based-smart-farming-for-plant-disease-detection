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

class Login:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def verifyLogin(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM farmer WHERE USERNAME = %s AND PASSWORD = %s', (self.__username, self.__password))
        farmer = cursor.fetchall()

        cursor.execute('SELECT * FROM admin WHERE USERNAME = %s AND PASSWORD = %s', (self.__username, self.__password))
        admin = cursor.fetchall()

        cursor.execute('SELECT * FROM expertadvisor WHERE USERNAME = %s AND PASSWORD = %s', (self.__username, self.__password))
        expadv = cursor.fetchall()

        if farmer:
            result = 1
            data = farmer
        elif admin:
            result = 2
            data = admin
        elif expadv:
            result = 3
            data = expadv
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
