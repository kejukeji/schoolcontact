# coding: UTF-8
__author__ = 'Juingya'

from flask import request,render_template,flash,url_for,redirect
from SchoolContact.models.students import StudentsClass
from SchoolContact.services.student_service import *
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
    check_student_is_none(student)
    return render_template('message_of_you.html',student = student)



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
    check_student_is_none(student)
    temp_str = ''
    if student.stu_enter_time:
        student.stu_enter_time = str(student.stu_enter_time)[0:10]
    if student.stu_enter_time == None:
        student.stu_enter_time = temp_str
    if student.stu_company == None:
        student.stu_company = temp_str
    if student.industry == '':
        student.industry = temp_str
    if student.stu_position == None:
        student.stu_position = temp_str
    if student.stu_contact == None:
        student.stu_contact = temp_str
    return render_template('change_message.html',student=student)


def change_message(stu_id):
    student = get_stu_by_id(stu_id)
    student.stu_enter_time =request.form.get('e_time')
    student.stu_company = request.form.get('company')
    student.industry_id = int(request.form.get('trade'))
    student.stu_position =request.form.get('position')
    student.stu_contact =request.form.get('mail')
    add(student)
    return redirect(url_for('show_message',stu_id=stu_id))


