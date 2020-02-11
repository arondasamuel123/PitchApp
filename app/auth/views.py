from flask import render_template,redirect,url_for
from app.models import User
from .forms import RegistrationForm
from .. import db
from . import auth 
from werkzeug.security import generate_password_hash


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email= form.email.data, username= form.username.data,pass_secure= generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        
        return "Your record has been entered "
        # return redirect(url_for('auth.login'))
        
        return render_template('auth/register.html',registration_form = form)


@auth.route('/login', methods = ["GET", "POST"])
def login():
    return render_template('auth/login.html')