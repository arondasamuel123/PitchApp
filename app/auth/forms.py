from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User




class RegistrationForm(FlaskForm):
    email = StringField('Enter your Email Address', validators=[Required(), Email()])
    username = StringField('Enter your Username', validators=[Required()])
    password = PasswordField('Enter your Password', validators=[Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')
    
    
    def validate_email(self, data_field):
        if User.query.filter_by(email= data_field.data).first():
            raise ValidationError('There is already an account with this email')
        
    def validate_username(self, data_field):
        if User.query.filter_by(username= data_field.data).first():
            raise ValidationError('The username has been taken')
        
class LoginForm(FlaskForm):
    email = StringField("Enter your Email", validators=[Required()])
    password = PasswordField("Enter your password", validators=[Required()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField('Sign In')
    
        
    