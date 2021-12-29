from flask import (render_template, Flask, request, redirect, url_for, session)
from . import routes

class Logout:
    @routes.route('/logout')
    def logout():
        session.pop('id', None)
        session.pop('fullname', None)
        session.pop('username', None)
        session.pop('roles', None)

        return redirect(url_for('index'))
