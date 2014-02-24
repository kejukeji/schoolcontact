__author__ = 'Juingya'
from flask import  render_template
def login():
    return render_template('login.html')
def register():
    return render_template('register.html')