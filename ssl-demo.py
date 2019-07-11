from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/get")
def gary():
    return "get OK!"


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == "gary" and request.form['password'] == "123456":
            print (request.form['username'])
            return "OK!!"
        else:
            print (request.form['username'])
            print (request.form['password'])
            return 'Invalid username/password'
