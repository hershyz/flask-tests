from flask import Flask, redirect, url_for, render_template, request
from flask.globals import session

app = Flask(__name__)
app.secret_key = "aaaaa" # secret key neccesary for using sessions

@app.route("/")
def home():
    return "<h1>home page</h1>"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return "<h1>" + str(user) + "</h1>"
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run()