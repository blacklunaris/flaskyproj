
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    biography = StringField('Biography', validators=[DataRequired()])


class PhotoForm(FlaskForm):
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
    description = StringField('Description', validators=[DataRequired()])