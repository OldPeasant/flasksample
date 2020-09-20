from configparser import ConfigParser
from flask import Flask, send_from_directory
import os

config = ConfigParser()

try:
    config.read(os.path.expanduser('~/.flasktest'))
    wiki_user = config.get('confluence', 'user')
    wiki_password = config.get('confluence', 'password')
except:
    print("Error reading properties:")
    print("Expecting config file ~/.flasktest with section confluence and properties user, password")
    exit(1)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/<string:filename>')
def serve_static(filename):
    return send_from_directory("static", filename)

if __name__ == '__main__':
    app.run()

