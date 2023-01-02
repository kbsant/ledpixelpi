from flask import Flask
from markupsafe import escape
#import board
#import neopixel

#pixels = neopixel.NeoPixel(board.D18, 64)


app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><a href="static/paint.html">led pixel pi</p></body></html>'

@app.route('/px/<int:index>/<int:red>/<int:green>/<int:blue>')
def px(index, red, green, blue):
    #pixels[int(index)] = (int(red)/4,int(green)/4,int(blue)/4)
    return f'Hello, i={index} r={red} g={green} b={blue}!'
