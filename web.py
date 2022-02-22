import flask
import requests

from datetime import datetime

app = flask.Flask(__name__, static_url_path='/')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/search')
def login():
    return flask.render_template('search.html')

@app.route('/song')
def song():
    try:
        text = requests.get(f'https://api.textyl.co/api/lyrics?q={flask.request.args.get("search")}').json()
        text = [t['lyrics'] for t in text]

    except:
        text = ['Song wurde nicht gefunden.']

    return flask.render_template('song.html', text=text)

app.run(port=2222, debug=True)