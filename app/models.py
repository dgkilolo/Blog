from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(writer_id):
    return Writer.query.get(int(writer_id))


class Writer(UserMixin, db.Model):
    __tablename__ = 'writer'    
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)    
    
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())    
    # password_hash = db.Column(db.String(255))
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


class Posts(db.Model):
  
  __tablename__ ='posts'

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  description = db.Column(db.String(700))
  posted = db.Column(db.DateTime, default=datetime.utcnow)  
#   user_id = db.Column(db.Integer, db.ForeignKey('writer.id'))
#   category = db.Column(db.String(255))
  comments = db.relationship('Comments',backref = 'commentPost',lazy="dynamic")
  

  def save_post(self):

    db.session.add(self)
    db.session.commit()

#   def get_comment(self):
#     pitches = Pitch.query.filter_by(id = self.id).first()
#     comments = Comment.query.filter_by(pitch_id = pitch.id).all()    
#     return comments 

#   @classmethod
#   def get_post(cls,category):
#     pitches = Pitch.query.filter_by(category=category).all()
#     return pitches  

  @classmethod
  def get_post(cls,id):
    post=Posts.query.filter_by(id=id).first()
    return post


class Comments(db.Model):
  '''
  this class defines characteristics of a comment
  '''
  __tablename__ = 'comments'
  
  id = db.Column(db.Integer, primary_key = True)
  comment = db.Column(db.String(255))
  time = db.Column(db.DateTime, default=datetime.utcnow) 
  # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

  def save_comments(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments_by_post(cls,id):
    '''
    function to gets comments based on their post_id
    '''
    comments_list = Comments.query.filter_by(post_id = id).all()

    return comments_list
  

  def __repr__(self):
    return f'Comment {self.comment}'


class Quotes:
  '''
  Quotes class that defines the quotes objects
  '''

  def __init__ (self, author, quote):
    self.author = author
    self.quote = quote