import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello </h1>"

app.run(os.getenv('IP'), port=(os.getenv('PORT')), debug=True)