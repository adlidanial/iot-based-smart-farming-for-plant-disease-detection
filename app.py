from flask import Flask, render_template
from routes import *
from flaskext.mysql import MySQL
from routes.connect import HOST, USER, PASSWORD, DB

app = Flask(__name__)
app.register_blueprint(routes)
app.secret_key = '_5#y2L"F4Q8z]/'
app.config['MAX_CONTENT_PATH'] = 2 * 1000 * 1000 # Max File Upload:2 MB

app.config['MYSQL_DATABASE_HOST'] = HOST
app.config['MYSQL_DATABASE_USER'] = USER
app.config['MYSQL_DATABASE_PASSWORD'] = PASSWORD
app.config['MYSQL_DATABASE_DB'] = DB

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template('index.html')