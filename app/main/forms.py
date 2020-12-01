from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    project_name = StringField('Your Project\'s name', validators = [Required()])
    pitch_description = TextAreaField('Project Pitch ', validators = [Required()])
    submit = SubmitField('Submit')