__author__ = 'Juingya'
#coding: utf-8

from flask import request,render_template,flash,url_for,redirect
from SchoolContact.models.students import StudentsClass
from SchoolContact.services.student_service import *
import hashlib


def reset_password(stu_id):
    student = get_stu_by_id(stu_id)
    password =  hashlib.new('md5', request.form.get('password')).hexdigest()
    student.stu_password = password
    add(student)
    flash(u'密码已修改，重新登录吧')
    return render_template('login.html')



