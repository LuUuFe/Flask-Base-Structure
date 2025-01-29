from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class UserForm(FlaskForm):
    name = StringField(
        "Enter your name",
        validators=[
            DataRequired(message="Please enter a name"),
            Length(min=1, max=50, message="Name must be between 1 and 50 characters"),
        ],
    )
    email = StringField(
        "Enter your email",
        validators=[
            DataRequired(message="Please enter an email"),
            Email(message="Invalid email address"),
        ],
    )
    submit = SubmitField("Submit")
