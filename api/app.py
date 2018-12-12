#!flask/bin/python
import json
from flask import Flask

app = Flask(__name__)

@app.route('/list')
def index():
    return json.dumps({"hello": "world"})
