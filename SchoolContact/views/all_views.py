# coding: UTF-8
from flask import  render_template, request
def login():
    return render_template('login.html')
def register():
    openid = request.args.get('openid', '没有获取到openid')
    return render_template('register.html',
                           openid=openid)
#返回按条件查询校友页面
def select():
     return render_template('search.html')
