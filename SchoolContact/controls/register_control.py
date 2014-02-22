# coding: UTF-8
__author__ = 'Juingya'

from flask import request,render_template,flash,url_for,redirect
from schoolcontact.models import *
from schoolcontact.services.student_service import *
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
    return render_template('message_of_you.html',student = student)



def html_form(form):
      mobile = request.form.get('inputMobile')
      password = request.form.get('password')
      repassword = request.form.get('repassword')
      if query(mobile):
          return False
      elif password == repassword:
          return Student(stu_tel = mobile,
                           stu_name = form.get('stu_name'),
                           stu_password =  hashlib.new('md5', form.get('password')).hexdigest())
      else:
          return 'error'

def login_in():
    mobile = request.form.get('inputMobile')
    password =  hashlib.new('md5',request.form.get('password')).hexdigest()
    if query_student(mobile,password):
        student = query_student(mobile,password)
        return render_template('message_of_you.html',student= student)
    else:
        flash(u'用户名或密码错误')
        return render_template('login.html')

def save_message(stu_id):
    stu = get_stu_by_id(stu_id)
    stu.stu_enter_time = request.form.get('e_time')
    stu.stu_company = request.form.get('company')
    stu.stu_trade = request.form.get('trade')
    stu.stu_position = request.form.get('position')
    stu.stu_contact = request.form.get('mail')
    add(stu)
    return redirect(url_for('show_message',stu_id = stu_id))