__author__ = 'Juingya'
# coding:utf-8
from flask import  render_template, request
from SchoolContact.models.user_attention import *
from SchoolContact.services.student_service import *

def concerned_page(stu_id):
    current_page = request.args.get('current_page')
    user_concerned_count = get_user_by_stu_id_count(stu_id)
    user_concerned = get_user_by_stu_id(stu_id)
    students =[]
    if user_concerned_count > 1:
        for i in user_concerned:
            student = get_stu_by_id(i.followers)
            students.append(student)
    elif user_concerned_count ==1:
        students = get_stu_by_id(user_concerned.followers)
    else:
        pass
    per_page=5
    max_page= (user_concerned_count-1)/per_page+1
    return render_template('/concerned_page.html',students = students,user_concerned_count=user_concerned_count)


