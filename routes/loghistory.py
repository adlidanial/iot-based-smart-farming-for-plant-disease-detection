from flask import (render_template, Flask, request, redirect, url_for, session)
from flaskext.mysql import MySQL
from . import routes

app = Flask(__name__)

mysql = MySQL(app)

class LogHistory:
    @routes.route('/log-history')
    def loghistory():
        return render_template('log-history.html')
