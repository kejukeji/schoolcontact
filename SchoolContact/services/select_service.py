# coding: UTF-8

from SchoolContact.models.students import StudentsClass
from SchoolContact import db


def get_student_all():
    '''获取所有学生'''
    student_all = StudentsClass.query.filter().all()
    return student_all


def get_student_by_industry(industry):
    '''根据行业获取'''
    student_count = StudentsClass.query.filter(StudentsClass.stu_trade == industry).count()
    if student_count > 1:
        student = StudentsClass.query.filter(StudentsClass.stu_trade == industry).all()
    else:
        student = StudentsClass.query.filter(StudentsClass.stu_trade == industry).first()
    return student