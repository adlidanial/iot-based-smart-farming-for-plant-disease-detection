from flask import (render_template, session)
from flaskext.mysql import MySQL
from . import routes

class Dashboard: 

    @routes.route('/dashboard')
    def dashboard():

        return render_template('dashboard.html')