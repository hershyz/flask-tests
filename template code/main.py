from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("template1.html")

@app.route("/<name>")
def name(name):
    return render_template("template2.html", content=name)

if __name__ == "__main__":
    app.run()