from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {
        'nickname': 'Billy Wilson'
    }

    return '''
        <!DOCTYPE html>
        <html lang="en">
            <head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="IE=Edge">

		<title>Billy Wilson Arante | Home</title>

            </head>
            <body>

		<h1>Hello, ''' + user['nickname'] + '''</h1>

            </body>
        </html>
    '''
