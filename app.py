from flask import Flask, render_template, request, redirect, url_for
import requests
import services
from flask_login import LoginManager , UserMixin, login_required,login_user

app = Flask(__name__)
app.secret_key = 'your_secret_key' 
login_manager = LoginManager(app)

# Simple User class for Flask-Login
class User(UserMixin):
    def __init__(self, user_id,token):
        self.id = user_id
        self.token = token

# User loader callback function
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# LOGIN SECTION - START
@app.route("/")
def index():
    return render_template("pages/samples/login.html")

api_url = "https://bapi.beeclue.com/businesses/users/signin"

@app.route("/loginHandler", methods=["POST"])
def loginHandler(): 
    username = request.form.get('username')
    password = request.form.get('password')







# LOGIN SECTION - END


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
