from flask import (render_template, Flask, request, redirect, url_for, session)
from flaskext.mysql import MySQL
from . import routes

app = Flask(__name__)

mysql = MySQL(app)

class Profile:
    @routes.route('/profile')
    def profile():
        return render_template('profile.html')
