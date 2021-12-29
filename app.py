from flask import Flask, render_template
from routes import *
from flaskext.mysql import MySQL

app = Flask(__name__)
app.register_blueprint(routes)
app.secret_key = '_5#y2L"F4Q8z]/'
app.config['MYSQL_HOST'] = 'us-cdbr-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'b1646d0d089bab'
app.config['MYSQL_PASSWORD'] = '94ed5161'
app.config['MYSQL_DB'] = 'heroku_bd37171be9fe3d6'

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template('index.html')