# coding: utf-8


from flask import make_response, request
from xml.etree import ElementTree as ET
from .webchat import WebChat
from .tools import *
from sqlalchemy import desc

import string





BASE_URL = "http://bilibili.kejukeji.com"
HELP = "感谢关注客聚科技平台，输入'h'获取帮助信息"

