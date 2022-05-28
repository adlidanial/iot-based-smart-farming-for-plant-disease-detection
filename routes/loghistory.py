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

class LogHistory:
    @routes.route('/log-history')
    def loghistory():
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT LOGHISTORY.PK_ID, LOGHISTORY.FK_ID_FARMER, LOGHISTORY.FK_ID_DISEASE, LOGHISTORY.URL_IMAGE, '
        +'FARMER.PK_ID, PLANTDISEASE.PK_ID, PLANTDISEASE.PLANT_NAME, PLANTDISEASE.PLANT_DISEASE '
        +'FROM LOGHISTORY '
        +'INNER JOIN FARMER ON LOGHISTORY.FK_ID_FARMER = FARMER.PK_ID '
        +'INNER JOIN PLANTDISEASE ON LOGHISTORY.FK_ID_DISEASE = PLANTDISEASE.PK_ID '
        +'WHERE LOGHISTORY.FK_ID_FARMER = %s', (session['id']))
        data = cursor.fetchall()


        return render_template('log-history.html', data = data)
