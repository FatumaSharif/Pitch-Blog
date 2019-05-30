from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manger


@login_manger.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class Pitch(db.Model):
  __tablename__ = 'pitch'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  category = db.Column(db.String(255))  
  pitch = db.Column(db.String(255))
  posted = db.Column(db.Time, default=datetime.utcnow())
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

  def save_pitch(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_pitch(cls, id):
    pitch = Pitch.query.filter_by(id=id).all()
    return pitch


class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), index=True)
  email = db.Column(db.String(255), unique=True, index=True)
  password_hash = db.Column(db.String(255))
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  pitch = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
  comment = db.relationship('Comment', backref='user', lazy='dynamic')

  @property
  def password(self):
      raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
      self.password_hash = generate_password_hash(password)

  def verify_password(self,password):
      return check_password_hash(self.password_hash,password)

  def __repr__(self):
    return f'User {self.username}'


class Comment(db.Model):
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  comment = db.Column(db.String(255))
  posted = db.Column(db.Time, default=datetime.utcnow())
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

  def __repr__(self):
    return f'User (self.name)'

  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comment(cls,id):
    comments = Comment.query.filter_by(pitch_id=id).all()
    return comments
