from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError
from ..models import Pitch


class PitchForm(FlaskForm):
    # pitch_choices =[('promotion-pitch', 'Promotion Pitch'), ('interview-pitch, Interview Pitch'),('mvp-pitch, MVP pitch '),('pickup-lines', 'Pickup Lines')]
    pitch_cat = SelectField(u'Pitch Type', choices=[('Interview-Pitch', 'Interview'), ('Promotion-Pitch', 'Promotion'), ('Product-Pitch', 'Product')],validators=[Required()])
    pitch = TextAreaField('Enter your pitch', validators=[Required()])
    submit = SubmitField('Pitch')
    
    
    
