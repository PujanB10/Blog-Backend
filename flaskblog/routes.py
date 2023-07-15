from flaskblog.models import User, Post
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app, db, bcrypt

posts = [
    {
        "name":"Pujan Bhattarai",
        "title":"My First Blog",
        "date":"20 November, 2020",
        "content":"First Content"
    },
      {
        "name":"Rajan Bhattarai",
        "title":"My Second Blog",
        "date":"14 December, 2020",
        "content":"Second Content"
    },
      {
        "name":"Sujan Bhattarai",
        "title":"My Third Blog",
        "date":"10 october, 2020",
        "content":"Third Content"
    }

]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title="Hello")


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login UNsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
