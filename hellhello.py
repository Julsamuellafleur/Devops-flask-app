


from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <h1>Hello, World, I am a Flask app!</h1>
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
