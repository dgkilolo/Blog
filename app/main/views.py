from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_quote
from ..models import Writer, Posts
from flask_login import login_required, current_user
from .forms import UpdateProfile, NewPost
from .. import db
# import markdown2

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting quote
    quote = get_quote()

    title = 'Blog'

    return render_template('index.html', title = title, quote=quote  )
    

@main.route('/home')
def home():
    '''
    View root page function that returns the home page.
    '''
    title = 'Blog'
    posts = Posts.query.all()
    # pitches = Pitch.query.filter_by(category = 'pun').all()
    # comment = Comment.query.filter_by(pitch_id = 1).all()
    
    return render_template('home.html', title = title, posts=posts)

@main.route('/writer/<uname>')
def profile(uname):
    writer = Writer.query.filter_by(username = uname).first()

    if writer is None:
        abort(404)

    # pitches=Pitch.query.filter_by(user_id=user.id).all()
    # category=Pitch.query.filter_by(category = " ").all()

    return render_template("profile/profile.html", writer=writer)


@main.route('/writer/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    writer = Writer.query.filter_by(username = uname).first()
    if writer is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        writer.bio = form.bio.data

        db.session.add(writer)
        db.session.commit()

        return redirect(url_for('.profile',uname=writer.username))

    return render_template('profile/update.html',form =form)


@main.route('/post', methods = ['GET','POST'])
@login_required
def add_pitch():
  
  form = NewPost()
  if form.validate_on_submit():
    title = form.title.data
    post = form.post.data  
    
    # Updated post instance
    new_post = Posts(title=title,description=post)

    # Save post method
    new_post.save_post()
    return redirect(url_for('.home'))

  title = 'New post'
  return render_template('newpost.html',title = title,pitch_form=form )





# @main.route('/quotes')
# def quote():

#     '''
#     View root page function that returns the quote page and its data
#     '''
#     title = 'Pitch'
#     pitches = Pitch.query.filter_by(category = 'quote').all()
#     comment = Comment.query.filter_by(pitch_id = 3).all()
#     return render_template('quotes.html', title = title, pitches = pitches, comment=comment)

# @main.route('/twister')
# def twister():

#     '''
#     View root page function that returns the tongue twister page and its data
#     '''
#     title = 'Pitch'
#     pitches = Pitch.query.filter_by(category = 'tongue twister').all()
#     comment = Comment.query.filter_by(pitch_id = 4).all()
#     return render_template('twister.html', title = title, pitches = pitches, comment=comment)







# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

# @main.route('/puns/new/<userID>', methods = ['GET','POST'])
# @login_required
# def add_pitch(userID):
#   user = User.query.filter_by(username = userID).first()  
#   form = NewPitch()
#   if form.validate_on_submit():
#     title = form.title.data
#     pitch = form.pitch.data  
#     category = form.category.data

#     # Updated pitch instance
#     new_pitch = Pitch(title=title,description=pitch, user_id = user.id, category = category)

#     # Save pitch method
#     new_pitch.save_pitch()
#     return redirect(url_for('.pun'))

#   title = 'New pitch'
#   return render_template('newpitch.html',title = title,pitch_form=form )


# @main.route('/puns/new/<userID>/comment', methods = ['GET','POST'])  
# @login_required
# def add_comment(userID):
#   user = User.query.filter_by(username = userID).first() 
#   # pitch = Pitch.query.filter_by(id = pitch_id).first()
#   form = Feedback()
#   if form.validate_on_submit():
    

#     comment = form.comment.data

#     # Updated comment instance
#     new_comment = Comment(comment=comment, user_id = user.id)

#     # Save comment method
#     new_comment.save_comment()
    
#     return redirect(url_for('.pun'))
  
#   return render_template('newcomment.html' ,comment_form = form )


# @main.route('/quotes/new/<userID>', methods = ['GET','POST'])
# @login_required
# def add_pitched(userID):
#   user = User.query.filter_by(username = userID).first()  
#   form = NewPitch()
#   if form.validate_on_submit():
#     title = form.title.data
#     pitch = form.pitch.data     
#     category = form.category.data

#     # Updated pitch instance
#     new_pitch = Pitch(title=title,description=pitch, user_id = user.id, category = category)

#     # Save pitch method
#     new_pitch.save_pitch()
#     return redirect(url_for('.quote'))

#   title = 'New pitch'
#   return render_template('newpitch.html',title = title,pitch_form=form )


# @main.route('/quotes/new/<userID>/comment', methods = ['GET','POST'])  
# @login_required
# def add_commented(userID):
  
#   form = Feedback()
#   if form.validate_on_submit():
    
#     comment = form.comment.data

#     # Updated comment instance
#     new_comment = Comment(comment=comment)

#     # Save comment method
#     new_comment.save_comment()
    
#     return redirect(url_for('.quote'))
  
#   return render_template('newcomment.html' ,comment_form = form )

  

# @main.route('/twister/new/<userID>', methods = ['GET','POST'])
# @login_required
# def add_pitches(userID):
#   user = User.query.filter_by(username = userID).first()  
#   form = NewPitch()
#   if form.validate_on_submit():
#     title = form.title.data
#     pitch = form.pitch.data     
#     category = form.category.data

#     # Updated pitch instance
#     new_pitch = Pitch(title=title,description=pitch, user_id = user.id, category = category)

#     # Save pitch method
#     new_pitch.save_pitch()
#     return redirect(url_for('.twister'))

#   title = 'New pitch'
#   return render_template('newpitch.html',title = title,pitch_form=form )


# @main.route('/twister/new/<userID>/comment', methods = ['GET','POST'])  
# @login_required
# def add_commentes(userID):
  
#   form = Feedback()
#   if form.validate_on_submit():
    
#     comment = form.comment.data

#     # Updated comment instance
#     new_comment = Comment(comment=comment)

#     # Save comment method
#     new_comment.save_comment()
    
#     return redirect(url_for('.twister'))
  
#   return render_template('newcomment.html' ,comment_form = form )

