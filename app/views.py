from flask import render_template
from app import app

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
