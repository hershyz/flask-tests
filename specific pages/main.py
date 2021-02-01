from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>daby</h1>"

@app.route("/<name>")
def user(name):
    return "hello " + str(name)

if __name__ == "__main__":
    app.run()
