from flask import render_template, redirect, url_for
from . import main
from .forms import PitchForm
from ..models import User, Pitch
from .. import db

@main.route("/")
def index():
    '''
    View function that return index html file
    '''

    all_category = ['Software Engineering', 'Business', 'Information Technology', 'Management']

    return render_template('index.html', all_category = all_category)

@main.route('/pitch/new/<int:user_id>', methods = ['GET', 'POST'])
def create_pitch(user_id):
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        new_pitch = Pitch(project_name = pitch_form.project_name.data, pitch_description = pitch_form.pitch_description.data, category = pitch_form.category.data, user_id = user_id)
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('/pitch/new_pitch.html', pitch_form = pitch_form)

@main.route('/pitch/all/<category>', methods = ['GET'])
def get_all_pitch(category):
    all_pitch = Pitch.query.filter_by(category = category)
    if all_pitch:
        return render_template('/pitch/pitch_list.html', all_pitch = all_pitch)

    return render_template('/pitch/new_pitch.html')