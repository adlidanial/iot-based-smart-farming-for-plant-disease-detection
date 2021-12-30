from flask import (render_template, Flask, request, redirect, url_for, session)
from flaskext.mysql import MySQL
from . import routes

app = Flask(__name__)

mysql = MySQL(app)

class ContactUs:
    @routes.route('/contact-us')
    def contactus():
        return render_template('contact-us.html')
