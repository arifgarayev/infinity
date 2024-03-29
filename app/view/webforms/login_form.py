from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(max=25)])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

    def is_logged(self):
        return True
