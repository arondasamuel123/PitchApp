from flask import render_template,redirect, url_for
from . import main
from .forms import PitchForm, CommentForm
from flask_login import current_user, login_required
from ..models import Pitch,Comment

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

@main.route('/addcomment/<int:id>', methods = ["GET", "POST"])
@login_required
def add_comment(id):
    comment_form = CommentForm()
    pitch_comment = Pitch.query.get(id)
    if comment_form.validate_on_submit():
        new_comment = Comment(comment= comment_form.opinion.data, user=current_user,pitch=pitch_comment)
        new_comment.save_comment()

        return redirect(url_for('main.add_comment'))
    flash(u'Successfully added comment', 'success')
    return render_template('addcomments.html',comment_form=comment_form, pitch_comment=pitch_comment)

@main.route('/viewcomments/<int:id>')
@login_required
def fet_comments(id):
    fetch_comments = Comment.query.filter_by(pitch_id= id).all()
    
    return render_template('viewcomments.html', fetch_comments=fetch_comments)
    
@main.route('/profile/<int:id>')
def user_profile(id):
    # user = User.query.filter_by(id = id).first()
    
    pitches = Pitch.query.filter_by(user_id= id).all()
    
    return render_template('prof/profile.html', pitches=pitches)

    
    
    