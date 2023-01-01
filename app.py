from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><a href="static/paint.html">led pixel pi</p></body></html>'

@app.route('/px/<index>/<red>/<green>/<blue>')
def px(index, red, green, blue):
    #return f"Hello, i={escape(index)} r={escape(red)} g={escape(green)} b={escape(blue)}!"
    return f'Hello, i={index} r={red} g={green} b={blue}!'
