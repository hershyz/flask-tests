from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        return usr(user)
    else:
        return render_template("form.html")

@app.route("/<usr>")
def usr(usr):
    return "<h1>hello " + str(usr) + "</h1>"

if __name__ == "__main__":
    app.run(debug=True)