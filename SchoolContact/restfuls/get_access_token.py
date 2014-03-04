# coding: UTF-8
from flask import request, render_template
from SchoolContact.services.student_service import *
import urllib2
from urllib import urlencode
import json
import sys
reload(sys)

def get_token():
    '''获取token'''
    code = request.args.get('code') # 得到用户同意授权的code
    get_access_token_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx55970915710ceae8&secret=0a9fcd79087745628d8eb5dd5fb9c418&code='+ code +'&grant_type=authorization_code'
    access_token = urllib2.urlopen(get_access_token_url) # 访问此url得到token
    json_token = access_token.read() # 读取token

    token = json.loads(json_token)['access_token'] # 从读取到的json中通过key得到access_token值
    open_id = request.args.get('FromUserName') # 获得用户的openId

    get_user_info_url = 'https://api.weixin.qq.com/sns/userinfo?access_token='+ token +'&openid='+ open_id +'&lang=zh_CN'

    user_info_result = urllib2.urlopen(get_user_info_url) # 请求此url的结果
    json_user_info = user_info_result.read() # 得到json结果

    nickname = json.loads(json_user_info)['nickname'] # 得到用户的昵称
    avatar_img_url = json.loads(json_user_info)['headimgurl'] # 得到微信用户头像
    result = insert_user(nickname, open_id, avatar_img_url) # 调用service中添加用户方法
    check_student_is_none(result)
    if result != 'None':
        return render_template('message_of_you.html',
                               student=result)
    else:
        return """
        <html>
        <head><title>Error</title></head>
        <body>
            <h1>Error Internal system error</h1>
        </body>
        </html>
        """
