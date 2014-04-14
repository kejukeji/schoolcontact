# coding: UTf-8
from flask import request, render_template
from SchoolContact.services.select_service import *
from SchoolContact.services.student_service import *
from SchoolContact.models.industry import *

def to_select_page():
    '''到结识校友'''
    student_all = get_student_all() #得到所有学生信息
    if student_all:
        return render_template('all_student.html',
                               student_all=student_all)
    return render_template('all_student.html',
                           marked='yes')


#def select_student():
    #'''根据行业查找'''
    #industry = request.args.get('industry') # 获取web端传如参数
    #student_all = get_student_by_industry(industry)
    #return render_template('all_student.html',
     #                      student_all=student_all)

   # trade =int(request.form.get('trade'))
    #enter_time =request.form.get('e_time')
    #student_selected_count = select_student_count(enter_time,trade)
    #if student_selected_count > 1:
     #   student_selected = select_student_all(enter_time,trade)
    #else:
     #    student_selected = select_student_first(enter_time,trade)
    #return render_template('search.html',student_selected = student_selected,student_count = student_selected_count)


#关键字查询 ，模糊查询
def vague_select():

    trade = request.args.get('trade')   #获取参数行业
    para = request.args.get('para')     #获取搜索参数
    current_page = request.args.get('current_page')  #当前页
    page_number = request.args.get('page_type')        #翻页参数


    #返回全部行业的判断
    if trade == '0':
        student_count = vague_with_no_trade_count(para)
    else:
        student_count = vague_count(trade,para)


    if current_page == None:
        current_page =1
    else:
       current_page = int(current_page)
    if page_number == 'up':
        current_page = int(current_page) -1
    elif page_number=='next':
        current_page = int(current_page) +1
    else:
        pass

    per_page = 5 #每页显示条数

    max_page =(student_count-1)/per_page + 1
    if current_page > max_page or current_page <= 0:
        current_page = 1
    #beg_page = current_page
    #end_page = current_page +10-1

    if student_count > 1:
        if trade == '0':
           student_selected = vague_with_no_trade_all(para,current_page,per_page)
            #显示行业类型
           for student in student_selected:
                industry_type = get_industry_by_industry_id(student.industry_id)
                if industry_type:
                    student.industry_type = industry_type.industry_name
           #for s in student_selected:
           #    check_student_is_none(s,'等待完善')
           #    continue
        else:
            student_selected  = vague_all(trade,para,current_page,per_page)
            #显示行业类型
            for student in student_selected:
                industry_type = get_industry_by_industry_id(student.industry_id)
                if industry_type:
                    student.industry_type = industry_type.industry_name
            #for s in student_selected:
            #   check_student_is_none(s,'等待完善')
            #   continue
    else:
        if trade == '0':
            student_selected = vague_with_no_trade_first(para)
            industry_type = get_industry_by_industry_id(student_selected.industry_id)
            student_selected.industry_type= industry_type.indusrty_name
            #check_student_is_none(student_selected,'等待完善')
        else:
            student_selected = vague_first(trade,para)
            industry_type = get_industry_by_industry_id(student_selected.industry_id)
            student_selected.industry_type= industry_type.indusrty_name
            #check_student_is_none(student_selected,'等待完善')
    industry_count = Industry.query.filter().count()
    if industry_count > 1:
        industry = Industry.query.filter().all()
    else:
        industry = Industry.query.filter().first()

    trade = int(trade)


    return render_template('search.html',student_selected = student_selected,
                                            student_count = student_count,
                                            industry=industry,
                                            industry_count=industry_count,
                                            trade= trade,
                                            para = para,
                                            current_page = current_page,
                                            max_page= max_page,
                                            mark='mark'
                                            )

