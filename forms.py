from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired()])

    password = PasswordField("Password", validators=[validators.DataRequired()])