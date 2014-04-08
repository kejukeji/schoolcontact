# coding: utf-8

#from flask import flash
#from SchoolContact.restfuls.webchat import WebChat
#from SchoolContact.restfuls.cons_string import MENU_STRING
#
#
#def create_menu():
#    web_chat = WebChat('7345')
#    web_chat.update('wxd284e29c062a6ef1', '0ce6f47ff64fd28a808f2287fd101fba')
#
#
#    try:
#        web_chat.create_menu(MENU_STRING)
#    except:
#        flash(u"创建微信菜单失败，由于网速的问题会有偶尔的失败")
#
#
#def render_string(menu_string):
#    url = "http://school.kejukeji.com/weixin"
#    return menu_string.replace("$url$", url)
import urllib
import urllib2
from urllib import urlencode
import json
import sys
from SchoolContact.restfuls.webchat import *
reload(sys)
sys.setdefaultencoding('UTF-8')

appid = 'wxfe4205911fe92b3c'
secret = '60ff2a6b01671146c55f3f22387a6e39'

webChat = WebChat('1234',appid,secret)

# gettoken = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxfe4205911fe92b3c&secret=60ff2a6b01671146c55f3f22387a6e39'

#f = urllib2.urlopen( gettoken )
#
#
#stringjson = f.read()
#
#access_token = json.loads(stringjson)['access_token']

#print access_token

#posturl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + access_token

menu = """
{
   "button": [
       {
           "name": "我的",
           "sub_button": [
               {
                   "type":"click",
                   "name": "我的名片",
                   "key": "login"
               },
               {
                   "type":"click",
                   "name":"修改名片",
                   "key":"update"
               },
               {
                   "type":"click",
                   "name":"修改密码",
                   "key":"update_password"
               }
                    ]
       },
       {
           "name": "结识校友",
           "sub_button": [
               {
                   "type":"click",
                   "name": "查找校友",
                   "key": "select"
               },
               {
                   "type":"click",
                   "name": "已关注校友",
                   "key": "concerned"
               }


                    ]
       }
       ]
}
"""
webChat.delete_menu()
webChat.create_menu(menu)

#request = urllib2.urlopen(posturl, menu.encode('utf-8') )

#print request.read()
#from flask import request
#import json
#class MenuManager:
#    accessUrl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxd284e29c062a6ef1&secret=0ce6f47ff64fd28a808f2287fd101fba"
#    delMenuUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token="
#    createUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token="
#    getMenuUri="https://api.weixin.qq.com/cgi-bin/menu/get?access_token="
#    def getAccessToken(self):
#        f = request.urlopen(self.accessUrl)
#        accessT = f.read().decode("utf-8")
#        jsonT = json.loads(accessT)
#        return jsonT["access_token"]
#    def delMenu(self, accessToken):
#        html = request.urlopen(self.delMenuUrl + accessToken)
#        result = json.loads(html.read().decode("utf-8"))
#        return result["errcode"]
#    def createMenu(self, accessToken):
#        menu = """
#{
#   "button": [
#       {
#           "name": "校友录",
#           "sub_button": [
#               {
#                   "type":"view",
#                   "name": "登陆",
#                   "url":"http://school.kejukeji.com/login"
#               }
#                    ]
#       },
#       {
#           "name": "校友录",
#           "sub_button": [
#               {
#                   "type":"view",
#                   "name": "我的名片",
#                   "url":"http://school.kejukeji.com/login"
#               },
#               {
#                   "type":"view",
#                   "name": "搜索名片",
#                   "url":"http://school.kejukeji.com/register"
#               }
#                    ]
#       }
#       ]
#}
#
#
#
#"""
#        html = request.urlopen(self.createUrl + accessToken, menu.encode("utf-8"))
#        result = json.loads(html.read().decode("utf-8"))
#        return result["errcode"]
#    def getMenu(self):
#        html = request.urlopen(self.getMenuUri + accessToken)
#        print(html.read().decode("utf-8"))
#if __name__ == "__main__":
#    wx = MenuManager()
#
#    accessToken = wx.getAccessToken()
#
#    print(wx.delMenu(accessToken))   #删除菜单
#    #print(wx.createMenu(accessToken))  #创建菜单
#    wx.getMenu()
