from flask import Flask
from markupsafe import escape
#import board
#import neopixel

factor = 8
width = 8
height = 8
size = width * height
#pixels = neopixel.NeoPixel(board.D18, size)
app = Flask(__name__)

"""Translate from an array index to a board position, where pixels are strewn like a string"""
def board_pos(i):
    row = i // width
    col = i % width
    if row %2 == 1:
        # for odd rows, count columns from the left
        return (row * width) + col
    # for even rows, count columns from the right
    return (row * width) + width - col - 1


@app.route('/')
def index():
    return '<html><body><a href="static/paint.html">led pixel pi</p></body></html>'

@app.route('/px/<int:index>/<int:red>/<int:green>/<int:blue>')
def px(index, red, green, blue):
    pos = board_pos(index)
    #pixels[pos] = (red//factor,green//factor,blue//factor)
    return f'Hello at i={index} p={pos} r={red} g={green} b={blue}!'
