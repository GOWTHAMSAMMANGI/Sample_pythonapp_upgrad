from flask import Flask
myworld = Flask(__name__)
@myworld.route("/")
def run():
    return "{\"message\":\"Welcome to my Python World v1\"}"
if __name__ == "__main__":
    myworld.run(host="0.0.0.0", port=int("8000"), debug=True)