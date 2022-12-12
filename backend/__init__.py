from flask import Flask

app = Flask(__name__, static_folder='../instagram/build', static_url_path='/')

@app.route("/get")
def index():
    return "Hello Instagram"