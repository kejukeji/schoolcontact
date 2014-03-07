# coding: UTF-8

from flask import request, render_template
from SchoolContact.services.student_service import *
from SchoolContact.util.others import *


def followers(stu_id):
    '''关注'''
    insert_followers(request.form, stu_id)
    message = '已关注'
    return message
