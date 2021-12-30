from flask import (render_template, Flask, request, redirect, url_for, session)
from flaskext.mysql import MySQL
from . import routes

app = Flask(__name__)

mysql = MySQL(app)

class AboutUs:
    @routes.route('/about-us')
    def aboutus():
        return render_template('about-us.html')
