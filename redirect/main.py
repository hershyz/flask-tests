from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>daby</h1>"

@app.route("/<name>")
def user(name):
    return "hello " + str(name)

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="admin! (special)"))

if __name__ == "__main__":
    app.run()
