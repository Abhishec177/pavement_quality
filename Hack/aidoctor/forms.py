from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('NAME',validators=[DataRequired(), Length(min=2, max=20)])
    rollno = StringField('ROLL NUMBER',validators=[DataRequired(), Length(min=9, max=9)])
    password = PasswordField('PASSWORD',validators=[DataRequired()])
    confirm_password = PasswordField('COFIRM PASSWORD', validators=[DataRequired(),EqualTo('password')])
    hostel = SelectField('HOSTEL',choices=[('Agate','Agate'),('Garnet','Garnet'),('Diamond','Diamond')],validators=[DataRequired(), Length(min=2, max=20)])
    mess = SelectField('MESS',choices=[('A mess','A mess'),('B mess','B mess'),('C mess','C mess')],validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('REGISTER')


class LoginForm(FlaskForm):
    rollno = StringField('ROLL NUMBER',validators=[DataRequired(), Length(min=9, max=9)])
    password = PasswordField('PASSWORD',validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('LOGIN')
