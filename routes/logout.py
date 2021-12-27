from flask import (render_template, Flask, request, redirect, url_for, session)
from . import routes

class Logout:
    @routes.route('/logout')
    def logout():
        session['id'] = ''
        session['fullname'] = ''
        session['username'] = ''

        return redirect(url_for('index'))
