# coding: UTF-8
__author__ = 'Juingya'

from flask import request,render_template,flash,url_for,redirect
from SchoolContact.models.students import StudentsClass
from SchoolContact.services.student_service import *
from SchoolContact.restfuls.tools import *
from SchoolContact.util.session_common import *
import hashlib

def register_action():
    if request.method == 'POST':
       Student = html_form(request.form)
    if Student =='error':
        flash(u'密码不一致，请重新输入')
        return render_template('register.html')
    elif Student:
         add(Student)
         stu_id = Student.id
         flash(u'注册成功！')
         return redirect(url_for("show_message", stu_id= stu_id))
    else:
        flash(u'该号码已注册，换个号码试试或直接登录！')
        return render_template('register.html')


def show_message(stu_id):
    student = get_stu_by_id(stu_id)
    check_student_is_none(student,'等待完善')
    user_id = get_session('student_id')
    collect = request.args.get('collect','no')
    if collect == 'yes':
        insert_followers(request.form, stu_id)
    concerned = get_is_concerned(stu_id, user_id)
    if concerned:
        message = '已关注'
    else:
        message = '关注'
    if user_id == stu_id:
        return render_template('message_of_you.html',
                               student = student,
                               mark='')
    else:
        is_true = get_is_concerned_followers(stu_id) # 判断是否收藏
        if is_true:
            return render_template('message_of_you.html',
                                   student = student,
                                   mark='true',
                                   message=message)
        else:
            return render_template('message_of_you.html',
                               student = student,
                               mark='false',
                               message=message)



def html_form(form):
      mobile = request.form.get('inputMobile')
      password = request.form.get('password')
      repassword = request.form.get('password')
      if query(mobile):
          return False
      elif password == repassword:
          return Student(stu_tel = mobile,
                           stu_name = form.get('stu_name'),
                           stu_password =  hashlib.new('md5', form.get('password')).hexdigest(),
                           openid = form.get('openId'))
      else:
          return 'error'

def login_in():
    mobile = request.form.get('inputMobile')
    password =  hashlib.new('md5',request.form.get('password')).hexdigest()
    if query_student(mobile,password):
        student = query_student(mobile,password)
        set_session_user('student_id', student.id) # 登录后保存用户id
        return redirect(url_for('show_message',stu_id = student.id))
    else:
        flash(u'用户名或密码错误')
        return render_template('login.html')

def save_message(stu_id):

    stu = get_stu_by_id(stu_id)
    if stu.stu_enter_time == None:
         stu.stu_enter_time = request.form.get('e_time')

    if stu.stu_company ==None:
        stu.stu_company = request.form.get('company')

    if stu.industry_id ==None:
         stu.stu_trade = request.form.get('trade')

    if stu.stu_position ==None:
        stu.stu_position = request.form.get('position')

    if stu.stu_contact ==None:
       stu.stu_contact = request.form.get('mail')
    update(stu)
    return redirect(url_for('show_message',stu_id = stu_id))

def change(stu_id):
    student = get_stu_by_id(stu_id)
    check_student_is_none(student, '')
    industry, industry_count = get_industry() # 获得全部行业
    return render_template('change_message.html',
                           student=student,
                           industry=industry,
                           industry_count=industry_count)


def change_message(stu_id):
    student = get_stu_by_id(stu_id)
    param = ('stu_name','stu_tel','stu_enter_time','stu_company','industry_id','stu_position','stu_contact','account_qq',
    'account_wechat')
    dic = get_from_element(request.form, param) # 得到参数dictionary
    student.update(stu_name=dic['stu_name'], stu_tel=dic['stu_tel'], stu_enter_time=dic['stu_enter_time'],
                   stu_company=dic['stu_company'],industry_id=dic['industry_id'],stu_position=dic['stu_position'],
                   stu_contact=dic['stu_contact'],account_qq=dic['account_qq'],account_wechat=dic['account_wechat'])
    update(student) # 提交事物修改
    return redirect(url_for('show_message',stu_id=stu_id))