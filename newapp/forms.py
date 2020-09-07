from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField, BooleanField
#from wtfomrs.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                           Length(min=8, max=15) ])

    email = StringField('Email', validators[DataRequired(), Email()])

    password = PasswordField('Password', validators[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators[DataRequired(),EqualTo('password')])

    submit = SubmitField('Sing Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators[DataRequired(), Email()])
    password = PasswordField('Password', validators[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')
