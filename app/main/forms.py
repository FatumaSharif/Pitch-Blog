from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
  
  name = StringField('Your Name',validators=[Required()])
  category = StringField('Pitch Category', validators=[Required()])
  pitch = TextAreaField('Your Pitch', validators=[Required()])
  submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you', validators=[Required()])
  submit = SubmitField('Submit')


class CommentForm(FlaskForm):
  username = StringField('Your Name', validators=[Required()])
  comment = TextAreaField('Your Comment', validators=[Required()])
  submit = SubmitField('Submit')