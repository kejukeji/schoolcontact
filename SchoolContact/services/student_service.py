__author__ = 'Juingya'
# coding: UTF-8
from SchoolContact.models.students import StudentsClass as Student
from SchoolContact.models.database import *
from SchoolContact.models.industry import *
from sqlalchemy import desc


def add(Student):
    db.add(Student)
    db.commit()
def query(mobile):
    student = Student.query.filter(Student.stu_tel == mobile).first()
    return student
def query_student(mobile,password):
       stu = Student.query.filter(Student.stu_tel== mobile,Student.stu_password == password).first()
       if stu:
        return stu
       else:return False
def get_stu_by_id(stu_id):
    stu = Student.query.filter(Student.id == stu_id).first()
    industry = Industry.query.filter(Industry.id == stu.industry_id).first()
    stu.industry = ''
    if industry:
        stu.industry = industry.industry_name
    if stu:
        return stu
    else:return False


def update(Student):
    '''修改'''
    db.commit()


def get_student_by_openId(openId):
    '''根据openid查询用户'''
    student = Student.query.filter(Student.openid == openId).first() #
    if student:
        return str(student.id)
    return str(None)


def select_student_count(enter_time,industry_id):
     '''根据查询条件获取学生数'''
     student_selected_count = Student.query.filter(Student.stu_enter_time == enter_time,Student.industry_id==industry_id).count()
     return student_selected_count
def select_student_all(enter_time,industry_id):
    '''查询到多个学生'''
    student_selected = Student.query.filter(Student.stu_enter_time == enter_time,Student.industry_id==industry_id).all()
    return student_selected

def select_student_first(enter_time,industry_id):
    '''查询到一个学生 '''

    student_selected = Student.query.filter(Student.stu_enter_time == enter_time,Student.industry_id==industry_id).first()
    return student_selected



