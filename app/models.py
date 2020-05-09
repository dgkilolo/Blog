from . import db
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
# from . import login_manager
# from datetime import datetime

class User( db.Model):
    __tablename__ = 'users'
    
    # reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    # pitches=db.relationship('Pitch',backref='user',lazy="dynamic")
    # comment=db.relationship('Comment',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Quotes:
  '''
  Quotes class that defines the quotes objects
  '''

  def __init__ (self, author, quote):
    self.author = author
    self.quote = quote