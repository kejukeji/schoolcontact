# coding: UTF-8
from flask import request, render_template
from SchoolContact.services.student_service import *
from SchoolContact.restfuls.webchat import *
import urllib2
from urllib import urlencode
import json
import sys
reload(sys)

def get_token():
    '''获取token'''
    code = request.args.get('code') # 得到用户同意授权的code
    appid = 'wxfe4205911fe92b3c'
    secret = '60ff2a6b01671146c55f3f22387a6e39'
    weChat = WebChat('1234',appid, secret, code)
    result = weChat.oauth_user_info() # 得到授权后用户信息json字符串
    nickname = json.loads(result)['nickname'] # 得到你昵称
    header_image_url = json.loads(result)['headimgurl'] # 得到头像
    if result != 'None':
        return """
        <html>
        <head><title>profile</title></head>
        <body>
            <h1>%s</h1>
            <h2><img href='%s'/></h2>
        </body>
        </html>
        """ % (nickname, header_image_url)
    else:
        return """
        <html>
        <head><title>Error</title></head>
        <body>
            <h1>Error Internal system error</h1>
        </body>
        </html>
        """
