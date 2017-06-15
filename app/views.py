from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    new_user = {'nickname': 'Billy'}  # Mock data

    return render_template('index.html', user=new_user)
