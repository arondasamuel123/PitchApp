from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(225))
    email = db.Column(db.String(255),unique=True)
    pass_secure = db.Column(db.String(255))
    profile_image = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy='dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy= 'dynamic')
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    
    def password(self):
        raise AttributeError('You cant read password attribute')
    
    
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
    
    def __repr__(self):
        return f'User {self.username}'
    
class Pitch(db.Model):
    __tablename__ ='pitches'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    mintute_pitch = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'pitch', lazy= 'dynamic')
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    def get_pitch(cls, category):
        pitches = Pitch.query.filter_by(category=category).all()
        
        return pitches
    def get_pitches(cls, id):
        all_pitches = Pitch.query.filter_by(id = id).all()
        return all_pitches
    
class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    def get_comments(cls, pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()
        return comments
    