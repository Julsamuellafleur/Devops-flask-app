


from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''
<<<<<<< HEAD
    <h1>This is another string </h1>
=======
    <h1>Welcome</h1>
>>>>>>> new_greeting
    <p><a href="/about">About</a></p>
    <p><a href="/contact">Contact</a></p>
    '''


@app.route('/about')
def about():
    return '''
    <h1>About</h1>
    <p>This is my DevOps Flask application.</p>
    <p><a href="https://flask.palletsprojects.com/">Flask website</a></p>
    '''


@app.route('/contact')
def contact():
    return '''
    <h1>Contact</h1>
    <p>Email: D23125136@mytudublin.ie</p>
    <p><a href="/">Back to home</a></p>
    '''
