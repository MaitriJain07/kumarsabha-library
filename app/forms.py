from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField("नाम", validators=[DataRequired(), Length(max=100)])
    email = EmailField("ईमेल", validators=[DataRequired(), Email(), Length(max=120)])
    message = TextAreaField("संदेश", validators=[DataRequired(), Length(max=2000)])
