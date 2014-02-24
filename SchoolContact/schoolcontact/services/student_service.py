__author__ = 'Juingya'
# coding: UTF-8
from schoolcontact.models.students import StudentsClass as Student
from schoolcontact.models.database import *
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
    if stu:
        return stu
    else:return False



