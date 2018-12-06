from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    """Form for login"""
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

class PostForm(FlaskForm):
    """Form for posts"""
    title = StringField("Title", validators=[DataRequired(), Length(max=64)])
    body = TextAreaField("Write Your Post", validators=[DataRequired()])
    submit = SubmitField("Submit")

class EditAboutMeForm(FlaskForm):
    """Form for edit about me page"""
    body = TextAreaField("About Me", validators=[DataRequired()])
    submit = SubmitField("Submit")

    """ def __init__(self, original_body, *args, **kwargs):
    #     super(EditAboutMeForm, self).__init__(*args, **kwargs)
    #     self.original_body = original_body"""

class EditAboutThisBlogForm(FlaskForm):
    """Form for edit about this blog page"""
    body = TextAreaField("About This Blog", validators=[DataRequired()])
    submit = SubmitField("Submit")

    """# def __init__(self, original_body, *args, **kwargs):
    #     super(EditAboutThisBlogForm, self).__init__(*args, **kwargs)
    #     self.original_body = original_body"""
