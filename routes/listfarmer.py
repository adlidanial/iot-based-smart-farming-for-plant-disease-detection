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



class ListFarmer:
    def __init__(self, fullname, email, username, password):
        self.__fullname = fullname
        self.__email = email
        self.__username = username
        self.__password = password
    
    
    @routes.route('/listfarmer')
    def listfarmer():
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM FARMER')
        data = cursor.fetchall()

        return render_template('listfarmer.html', data = data)

    @routes.route('/listfarmer/edit/<editfarmer>', methods = ['GET', 'POST'])
    def editfarmer(editfarmer):
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM FARMER WHERE PK_ID = %s', (editfarmer))
        farmerdata = cursor.fetchall()

        print(farmerdata)

        pkid = farmerdata[0][0]
        name = farmerdata[0][1]
        email = farmerdata[0][2]
        username = farmerdata[0][3]
        password = farmerdata[0][4]

        if request.method == 'POST':
            pkid = request.form['id']
            name = request.form['name']
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']

            if(name != '' and email != '' and username != '' and password != ''):
                cursor = mysql.get_db().cursor()
                cursor.execute('UPDATE FARMER SET FULL_NAME = %s, EMAIL = %s, USERNAME = %s, PASSWORD = %s WHERE PK_ID = %s', (name, email, username, password, pkid))
                cursor.connection.commit()
        
                msgSuccess = True
                return redirect(url_for('.listfarmer'))
        return render_template('editfarmer.html', pkid = pkid, name = name, email = email, username = username, password = password)

    @routes.route('/listfarmer/delete/<deletefarmer>')
    def deletefarmer(deletefarmer):
        cursor = mysql.get_db().cursor()
        cursor.execute('DELETE FROM FARMER WHERE PK_ID = %s', (deletefarmer))
        cursor.connection.commit()

        return redirect(url_for('.listfarmer'))
