from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[DataRequired()])
    comment = TextAreaField('Pitch comment')  #We have removed ,validators=[DataRequired()]
    submit = SubmitField('submit')

# For login
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

# We update our bio to say something interesting about us.
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')





#ret
