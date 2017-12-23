from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {
        'nickname': 'Billy Wilson'
    }

    posts = [
    	{
	    'author': {'nickname': 'John'},
	    'body': 'Beautiful day in Portland!'
	},
	{
	    'author': {'nickname': 'Susan'},
	    'body': 'The Avengers movie was so cool!'
	},
	{
	    'author': {'nickname': 'Kevin'},
	    'body': 'Forrest Gump is one of my favorites.'
	},
	{
	    'author': {'nickname': 'Steph'},
	    'body': 'The Pursuit of Happyness was awesome to me.'
	}
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', title='Sign In', form=form)
