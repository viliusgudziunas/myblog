from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    post = TextAreaField("Say something", validators=[DataRequired()])
    submit = SubmitField("Submit")
