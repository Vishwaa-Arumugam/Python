from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, InputRequired, length, Email


class Forms(FlaskForm):
    username = EmailField("Email",  validators=[InputRequired("Please enter your email address."), DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), length(min=8)])
    Login = SubmitField("Login")
