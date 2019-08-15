from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,DateField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you')
    submit = SubmitField('Update bio')

class postChild(FlaskForm):
    name = TextAreaField('Input the name of your child',validators = [Required()])
    DoB = DateField('Enter your childs Date of birth',validators = [Required()],format ='%Y-%m-%d')
    submit = SubmitField('Submit')  