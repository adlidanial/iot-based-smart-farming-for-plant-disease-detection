from flask import (render_template, session)
from . import routes

class Home: 

    @routes.route('/')
    def index():
        
        if 'id' not in session:
            session.pop('id', None)

        return render_template('index.html')