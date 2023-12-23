from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators,IntegerField,DecimalField
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
class ClubForm(FlaskForm):
    club_code = StringField('Club Code', validators=[DataRequired(), Length(min=1, max=10)])
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=255)])
    total_market_value = DecimalField('Total Market Value (EUR)', validators=[NumberRange(min=0)])
    squad_size = IntegerField('Squad Size', validators=[NumberRange(min=0)])
    average_age = DecimalField('Average Age', validators=[NumberRange(min=0)])
    foreigners_number = IntegerField('Foreigners Number', validators=[NumberRange(min=0)])
    foreigners_percentage = DecimalField('Foreigners Percentage', validators=[NumberRange(min=0, max=100)])
    national_team_players = IntegerField('National Team Players', validators=[NumberRange(min=0)])
    stadium_name = StringField('Stadium Name', validators=[Length(max=255)])
    stadium_seats = IntegerField('Stadium Seats', validators=[NumberRange(min=0)])
    net_transfer_record = DecimalField('Net Transfer Record (EUR)', validators=[NumberRange(min=0)])
    coach_name = StringField('Coach Name', validators=[Length(max=255)])
    last_season = StringField('Last Season', validators=[Length(max=10)])
    url = StringField('URL', validators=[Length(max=255)])
    submit = SubmitField('Submit')