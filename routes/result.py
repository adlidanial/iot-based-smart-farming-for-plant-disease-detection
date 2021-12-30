from flask import (render_template, Flask, request, redirect, url_for, session)
from flaskext.mysql import MySQL
from . import routes

app = Flask(__name__)

mysql = MySQL(app)

class Result:
    @routes.route('/result')
    def result():
        return render_template('result.html')
