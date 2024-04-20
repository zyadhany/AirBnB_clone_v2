#!/usr/bin/python3
from flask import Flask, flash, redirect, render_template, request, session, send_file
from flask_session import Session

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", strict_slashes=False)
def root():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    return "C {}".format(text)

if __name__ == '__main__':
    app.run(debug=True)