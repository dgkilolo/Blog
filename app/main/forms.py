from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class NewPost(FlaskForm):
  title = StringField("Post Title", validators = [Required()])
  post = TextAreaField("Description", validators = [Required()])  
  
  submit=SubmitField("Add Post")

# class Feedback(FlaskForm):
#   comment = TextAreaField("Comment", validators=[Required()])
#   submit = SubmitField('Comment')