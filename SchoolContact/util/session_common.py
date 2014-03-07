# coding: UTF-8
from flask import session


def get_session(key):
    '''获取session中key的值'''
    if session.has_key(str(key)) and session[str(key)]:
        return session[str(key)]
    return None


def set_session_user(key_name, value_name):
    """
       登陆成功保存到session当中
    """
    session[str(key_name)] = value_name
