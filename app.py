import math 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign-up')
def signup():
    return render_template('sign-up.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)