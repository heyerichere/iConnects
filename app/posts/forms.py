from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField, DateField
from wtforms.validators import DataRequired, Length, Optional

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    content = TextAreaField("Content", validators=[DataRequired(), Length(min=1)])

    image = FileField("Upload Image", validators=[Optional()])
    video = FileField("Upload Video", validators=[Optional()])

    event_name = StringField("Event Name", validators=[Optional(), Length(max=100)])
    event_date = DateField("Event Date", validators=[Optional()])
    event_description = TextAreaField("Event Description", validators=[Optional(), Length(max=500)])

    # Submit button
    submit = SubmitField("Post")