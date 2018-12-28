from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from myproject.models import User  
from flask_wtf import FlaskForm



class LoginForm(FlaskForm):
    email = StringField('Email', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators =[DataRequired()])
    submit = SubmitField('Log IN ')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired(), EqualTo('pass_confirm', message = 'password must match')])
    pass_confirm = PasswordField('Confirm Password', validators =[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self,field):
        
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Your Email has alredy been used for Registration')
    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('This user name is already taken')
