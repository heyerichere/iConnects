from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from app.auth.models import Student, Alum 

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    content = TextAreaField("Content", validators=[DataRequired(), Length(min=1)])
    submit = SubmitField("Post")
