from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


# LOGIN SECTION - START
@app.route("/")
def index():
    return render_template("pages/samples/login.html")

@app.route("/login/handler/", methods=["POST"])
def loginHandler(): 
        # Set the URL for the login API
    url = "https://bapi.beeclue.com/businesses/users/signin"

    # Define the payload (username and password)
    payload = {
        "username": "username",
        "password": "password"
    }

    # Make a POST request to the login API
    response = requests.post(url, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response data (assuming it's in JSON format)
        data = response.json()

        # Extract the token from the response
        token = data.get("token")

        # Store the token in cookies or session for future requests
        # You can use a library like `requests.Session` for persistent sessions
        # For simplicity, we'll just print the token in this example
        print("Login successful. Token:", token)

        # You can now use this token for subsequent API requests in the session
    else:
        # If the login request was unsuccessful, print the error message
        print("Login failed. Error:", response.text)
    

# LOGIN SECTION - END


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
