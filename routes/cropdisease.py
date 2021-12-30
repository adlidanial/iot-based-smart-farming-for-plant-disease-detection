from flask import (render_template, Flask, request, redirect, url_for, session)
from flaskext.mysql import MySQL
from . import routes

app = Flask(__name__)

mysql = MySQL(app)

class CropDisease:
    @routes.route('/crop-disease')
    def cropdisease():
        return render_template('crop-disease.html')
