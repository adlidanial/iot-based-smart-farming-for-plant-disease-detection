from flask import Flask, render_template
from routes import *
from flaskext.mysql import MySQL

app = Flask(__name__)
app.register_blueprint(routes)
app.secret_key = '_5#y2L"F4Q8z]/'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'plant_disease_detection'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')