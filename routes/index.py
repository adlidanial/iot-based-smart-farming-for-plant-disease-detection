from flask import render_template
from . import routes

class Home: 

    @routes.route('/')
    def index():
        return render_template('index.html')