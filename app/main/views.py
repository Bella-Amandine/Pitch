from flask import render_template
from . import main

@main.route("/")
def index():
    '''
    View function that return index html file
    '''

    all_category = ['Software Engineering', 'Business', 'Information Technology', 'Management']

    return render_template('index.html', all_category = all_category)