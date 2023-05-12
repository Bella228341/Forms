from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

name = 'main'

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_reply = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remind_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Дії, які потрібно виконати при успішній валідації форми
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Дії, які потрібно виконати при успішній валідації форми
        return redirect(url_for('home'))
    return render_template('login.html', title='Log In', form=form)

@app.route('/home', methods=['GET', 'POST'])
def home():
    return 'Welcome to tha home page!'

if name == 'main':
    app.run(debug=True)
