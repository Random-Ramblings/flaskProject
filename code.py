# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'
@app.route("/hello")
def hello_world():
    return "Hello, World! The program runs :))"
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
    
if __name__=="__main__":
    app.run()