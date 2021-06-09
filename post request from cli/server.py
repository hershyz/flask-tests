from flask import Flask, request

app = Flask(__name__)

@app.route("/post_req", methods=["POST"])
def postreq():
    data = request.get_json()
    name = data['name']
    arr = data['mylist']
    return "your name is " + str(name) + " and the second element in the list is " + str(arr[1])

if __name__ == "__main__":
    app.run()