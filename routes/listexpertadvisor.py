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

class ListExpertAdvisor:
    def __init__(self, fullname, email, username, password):
        self.__fullname = fullname
        self.__email = email
        self.__username = username
        self.__password = password     

    @routes.route('/listexpertadvisor')
    def listexpertadvisor():
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM expertadvisor')
        data = cursor.fetchall()

        return render_template('listexpertadvisor.html', data = data)

    @routes.route('/listexpertadvisor/edit/<editexpertadvisor>', methods = ['GET', 'POST'])
    def editexpertadvisor(editexpertadvisor):
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM expertadvisor WHERE PK_ID = %s', (editexpertadvisor))
        data = cursor.fetchall()
        pkid = data[0][0]
        name = data[0][2]
        email = data[0][3]
        username = data[0][4]
        password = data[0][5]

        if request.method == 'POST':
            pkid = request.form['id']
            name = request.form['name']
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']

            if(name != '' and email != '' and username != '' and password != ''):
                cursor = mysql.get_db().cursor()
                cursor.execute('UPDATE expertadvisor SET FK_ID_ADMIN = %s, FULL_NAME = %s, EMAIL = %s, USERNAME = %s, PASSWORD = %s WHERE PK_ID = %s', (session['id'], name, email, username, password, pkid))
                cursor.connection.commit()
                msgSuccess = True
                return redirect(url_for('.listexpertadvisor'))
        return render_template('editexpertadvisor.html', pkid = pkid, name = name, email = email, username = username, password = password)

    @routes.route('/listexpertadvisor/delete/<deleteexpertadvisor>')
    def deleteexpertadvisor(deleteexpertadvisor):
        cursor = mysql.get_db().cursor()
        cursor.execute('DELETE FROM EXPERTADVISOR WHERE PK_ID = %s', (deleteexpertadvisor))
        cursor.connection.commit()

        return redirect(url_for('.listexpertadvisor'))
