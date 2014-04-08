__author__ = 'Juingya'
# coding:utf-8
from flask import  render_template, request
from SchoolContact.models.user_attention import *
from SchoolContact.services.student_service import *

def concerned_page(stu_id):
    user_concerned_count = get_user_by_stu_id_count(stu_id)
    user_concerned = get_user_by_stu_id(stu_id)
    students =[]
    if user_concerned_count > 1:
        for i in user_concerned:
            student = get_stu_by_id(i.followers)
            students.append(student)
    else:
        students = get_stu_by_id(user_concerned.followers)

    return render_template('/concerned_page.html',students = students)


