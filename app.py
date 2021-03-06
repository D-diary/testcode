import json

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient


# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.gangchu


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('main.html')


@app.route('/map')
def route_map():
    return render_template('map.html')


@app.route('/board')
def route_board():
    return render_template('board.html')


@app.route('/mypage')
def route_mypage():
    return render_template('mypage.html')


@app.route('/signup')
def route_signup():
    return render_template('signup.html')


@app.route("/login")
def route_login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
