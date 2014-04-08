# coding: utf-8


from flask import request, make_response
from xml.etree import ElementTree as ET
from .tools import parse_request
from .webchat import WebChat
from ..setting.wbb import BASE_URL
from SchoolContact.services.student_service import *
from .weixin_info import *
from ..util.session_common import *

import datetime

import string

def weixin():
    web_chat = WebChat('1234', APPID, SECRET)
    if request.method == "GET":
        if web_chat.validate(**parse_request(request.args, ("timestamp", "nonce", "signature"))):
            return make_response(request.args.get("echostr"))
        raise LookupError

    if request.method == "POST":
        # 这里需要验证 #todo
        xml_recv = ET.fromstring(request.data)
        MsgType = xml_recv.find("MsgType").text

        if MsgType == "event":
            return response_event(xml_recv, web_chat)
        if MsgType == "text":
            return response_text(xml_recv, web_chat, 1)
        if MsgType == 'voice':
            return response_voice(xml_recv, web_chat)


def response_voice(xml_receive, web_chat):
    '''对于用户语音进行处理'''
    recognition = xml_receive.find("Recognition").text
    toUserName = xml_receive.find("ToUserName").text # 得到接受者
    fromUserName = xml_receive.find("FromUserName").text # 得到发送者
    reply_dict = {
        "ToUserName": fromUserName,
        "FromUserName": toUserName,
        "CreateTime": 12345,
        "Content": recognition
    }
    return response(web_chat, reply_dict, 'text')


def response_text(xml_recv, web_chat, pub_id):
    """对于用户的输入进行回复"""
    Content = xml_recv.find("Content").text
    input_type = get_type(Content)

    if input_type in ('jia', 'gai'):
        return response_member_text(xml_recv, web_chat, pub_id, input_type)
    if input_type == '授权':
        return response_oauth(xml_recv, web_chat)

    # 下面的句子是鹦鹉学舌，后期改过来
    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text
    if input_type == '登录':
        Content = '<a href="http://school.kejukeji.com/login">点击登录</a>'

    reply_dict = {
            "ToUserName": FromUserName,
            "FromUserName": ToUserName,
            "CreateTime": 123,
            "Content": Content
    }
    return response(web_chat, reply_dict, "text")


def response_oauth(xml_receive, web_chat):
    '''授权'''
    Content = xml_receive.find("Content").text
    ToUserName = xml_receive.find("ToUserName").text
    FromUserName = xml_receive.find("FromUserName").text
    reply_dict = {
            "ToUserName": FromUserName,
            "FromUserName": ToUserName,
            "ArticleCount": 1,
            "item": [{
                "Title": '刮刮',
                "Description": '好玩',
                "PicUrl": BASE_URL + '/static/images/scratch_matter.jpg',
                "Url": 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxd66b61798e08ff5e&redirect_uri=scratch.kejukeji.com/oauth&response_type=code'
            }]
    }
    return response(web_chat, reply_dict, "news")


def response_event(xml_recv, web_chat):
    Event = xml_recv.find("Event").text
    EventKey = xml_recv.find("EventKey").text
    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text
    boolean = by_openId(FromUserName) # 根据openid判断是否存在
    Content = ''
    if boolean == 'None':
        dic = web_chat.get_user_info(FromUserName)
        result = insert_user(dic['nickname'],FromUserName, dic['img_url'])
        Content = '您还没绑定点击此连接进行<a href="http://school.kejukeji.com/show_message/%s?openid=yes">绑定</a>' %(result.id)

    reply_dict = response_event_message(FromUserName, ToUserName, Content)
    if (Event == 'CLICK') and (EventKey == 'login'):
        if boolean == 'None':
            pass
        else:
            Content = '请点击此链接<a href="' + BASE_URL + '/show_message/'+boolean+'?openid=yes">查看名片</a>'
        reply_dict = response_event_message(FromUserName, ToUserName, Content)
    if (Event == 'CLICK') and (EventKey == 'update'):
        if boolean == 'None':
            pass
        else:
            Content = '请点击此链接<a href="' + BASE_URL + '/change/'+boolean+'">修改名片</a>'
        reply_dict = response_event_message(FromUserName, ToUserName, Content)
    if (Event == 'CLICK') and (EventKey == 'update_password'):
        if boolean == 'None':
            pass
        else:
            Content = '请点击此链接<a href="' + BASE_URL + '/reset/'+boolean+'">修改密码</a>'
        reply_dict = response_event_message(FromUserName, ToUserName, Content)
    if (Event == 'CLICK') and (EventKey == 'select'):
        Content = '请点击此链接<a href="'+ BASE_URL +'/select_page">结识校友</a>'
        reply_dict = response_event_message(FromUserName, ToUserName, Content)
    if (Event == 'CLICK') and (EventKey == 'concerned'):
        Content = '请点击此链接<a href="'+ BASE_URL +'/concerned_page/'+boolean+'">结识校友</a>'
        reply_dict = response_event_message(FromUserName, ToUserName, Content)
    return response(web_chat, reply_dict, "text")


def response_event_message(FromUserName, ToUserName, Content):
    '''响应事件'''
    reply_dict = {
            "ToUserName": FromUserName,
            "FromUserName": ToUserName,
            "CreateTime": 1,
            "Content": Content
    }
    return reply_dict
def response_member_text(xml_recv, web_chat, pub_id, input_type):
    """如果用户输入jia或者是gai手机号码，这里进行判断"""
    Content = xml_recv.find("Content").text
    ToUserName = xml_recv.find("ToUserName").text
    FromUserName = xml_recv.find("FromUserName").text
    mobile = Content[3:]
    message = '测试'
    reply_dict = {
            "ToUserName": FromUserName,
            "FromUserName": ToUserName,
            "Content": message
        }
    return response(web_chat, reply_dict, "text")

def response(web_chat, reply_dict, reply_type):
    """通过返回的xml与类型，创建一个回复"""
    reply = web_chat.reply(reply_type, reply_dict)
    reply_response = make_response(reply)
    reply_response.content_type = 'application/xml'
    return reply_response


def by_openId(openId):
    '''得到openid获取用户'''
    boolean = get_student_by_openId(openId)
    return boolean


def get_type(Content):
    """返回用户输入的业务类型
    "jia" 或者 "gai" 值得是用户进行手机号码绑定与修改手机号码
    None 未知类型，不是相关的业务
    """
    if Content.startswith("jia"):
        return "jia"
    if Content.startswith("gai"):
        return "gai"
    if Content.startswith("授权"):
        return "授权"



HELP = "感谢关注客聚科技平台，输入'h'获取帮助信息"

