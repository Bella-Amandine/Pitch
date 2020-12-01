from flask import render_template
from . import main

@main.route("/")
def index():
    '''
    View function that return index html file
    '''

    return render_template('index.html')