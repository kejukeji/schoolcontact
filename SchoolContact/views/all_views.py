# coding: UTF-8
from flask import  render_template, request
def login():
    return render_template('login.html')
def register():
    openid = request.args.get('openId')
    return render_template('register.html',
                           openid=openid)