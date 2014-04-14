__author__ = 'Juingya'
# coding:utf-8
from flask import  render_template, request
from SchoolContact.models.user_attention import *
from SchoolContact.services.student_service import *

def concerned_page(stu_id):
    current_page = request.args.get('current_page') #当前页
    page_number = request.args.get('page_type')        #翻页参数

    if current_page == None:
        current_page =1
    else:
       current_page = int(current_page)
     #翻页
    if page_number == 'up':
        current_page = int(current_page) -1
    elif page_number=='next':
        current_page = int(current_page) +1
    else:pass

    user_concerned_count = get_user_by_stu_id_count(stu_id)
    user_concerned = get_user_by_stu_id(stu_id)
    students_all =[]
    per_page=5
    max_page= (user_concerned_count-1)/per_page+1
    if current_page > max_page or current_page < 1:
        current_page = 1
    else:
        pass

    if user_concerned_count > 1:
        for i in user_concerned:
            student = get_stu_by_id(i.followers)
            industry_type = get_industry_by_industry_id(student.industry_id)
            student.industry_type= industry_type.industry_name
            students_all.append(student)
            fro =(current_page-1) * 5 + 1
            to = current_page * 5+1
            students = students_all[fro:to]

    elif user_concerned_count ==1:
          students = get_stu_by_id(user_concerned.followers)
          industry_type = get_industry_by_industry_id(students.industry_id)
          students.industry_type= industry_type.industry_name
    else:
        pass



    return render_template('/concerned_page.html',students = students,
                                                       user_concerned_count=user_concerned_count,
                                                       current_page = current_page,
                                                       max_page= max_page,
                                                       stu_id = stu_id)


