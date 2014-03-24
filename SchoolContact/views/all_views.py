# coding: UTF-8
from flask import  render_template, request
from SchoolContact.models.industry import *
def login():
    return render_template('login.html')
def register():
    openid = request.args.get('openid', '没有获取到openid')
    return render_template('register.html',
                           openid=openid)
#返回按条件查询校友页面
def select():
    industry_count = Industry.query.filter().count()
    if industry_count >1:
        industry = Industry.query.filter().all()
    else:
        industry = Industry.query.filter().first()
    return render_template('search.html',industry_count=industry_count,industry=industry)
