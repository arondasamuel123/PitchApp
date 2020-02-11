from flask import render_template
from . import main
from .forms import PitchForm
from flask_login import current_user, login_required
from ..models import Pitch

@main.route('/')
def home():
    pitches = Pitch.query.all()
    return render_template('home.html',pitches=pitches)


@main.route('/add',methods = ["GET", "POST"])
@login_required
def add_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        p_category = pitch_form.pitch_cat.data
        create_pitch = Pitch(category= p_category, mintute_pitch=pitch_form.pitch.data, user=current_user)
        create_pitch.save_pitch()
        return redirect(url_for('main.home'))
    return render_template('pitch.html', pitch_form=pitch_form)


    
    
    