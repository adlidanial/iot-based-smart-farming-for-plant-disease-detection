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

class Dashboard: 

    @routes.route('/dashboard')
    def dashboard():
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT '+
            '(SELECT COUNT(PK_ID) FROM FARMER) AS COUNT_USER, ' +
            '(SELECT COUNT(PK_ID) FROM PLANTDISEASE) AS COUNT_PLANTDISEASE, '+
            '(SELECT COUNT(PK_ID) FROM EXPERTADVISOR) AS COUNT_EXPERTADVISOR ')
        data = cursor.fetchall()

        for row in data:
            userlogin = row[0]
            plantdisease = row[1]
            expadv = row[2]

        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT PLANT_DISEASE, DATE_CREATED FROM PLANTDISEASE')
        plant = cursor.fetchall()

        for row in plant:
            diseasename = row[0]
            datecreate = row[1]

        return render_template('dashboard.html', userlogin = userlogin, plantdisease = plantdisease, expadv = expadv, plant = plant)