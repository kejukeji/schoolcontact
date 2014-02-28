__author__ = 'Juingya'
#coding: utf-8
from flask import request,render_template,redirect
from SchoolContact.services.student_service import *
def reset_password_view(stu_id):
    student = get_stu_by_id(stu_id)
    return render_template('reset_password.html',student= student)

