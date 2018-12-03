from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

class PostForm(FlaskForm):
    title = StringField("Create Title", validators=[DataRequired(), Length(max=64)])
    body = TextAreaField("Write Your Post", validators=[DataRequired()])
    submit = SubmitField("Submit")
