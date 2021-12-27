from flask import render_template
from . import routes

class Register:

    @routes.route('/register')
    def register():
        return render_template('registration.html')