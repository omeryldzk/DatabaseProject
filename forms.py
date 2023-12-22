from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators,IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
class PlayerAttributesForm(FlaskForm):
    player_code = StringField('Player Code', validators=[DataRequired(), Length(min=1, max=50)])
    sub_position = StringField('Sub Position', validators=[Length(max=50)])
    position = StringField('Position', validators=[Length(max=50)])
    foot = StringField('Foot', validators=[Length(max=50)])
    height_in_cm = IntegerField('Height (cm)', validators=[NumberRange(min=0)])
    market_value_in_eur = IntegerField('Market Value (EUR)', validators=[NumberRange(min=0)])
    highest_market_value_in_eur = IntegerField('Highest Market Value (EUR)', validators=[NumberRange(min=0)])
    contract_expiration_date = StringField('Contract Expiration Date', validators=[Length(max=50)])
    submit = SubmitField('Submit')

class PlayerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    first_name = StringField('First Name', validators=[Length(max=50)])
    last_name = StringField('Last Name', validators=[Length(max=50)])
    submit = SubmitField('Submit')
