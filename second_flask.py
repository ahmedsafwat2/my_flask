from flask import Flask, render_template, url_for, flash, redirect, request
from form import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
app = Flask(__name__)
app.config['SECRET_KEY']='13f0f4f59bed30c2ea7c00bbfc6b0e1f'
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', posts=posts, title='ahmed')

@app.route("/register", methods=['GET', 'POST'])
def register():
    my_form = RegistrationForm()
    if request.method == 'POST':
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=my_form)

@app.route("/login")
def login():
    my_form = LoginForm()
    return render_template('login.html', title = 'Login', form=my_form)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
