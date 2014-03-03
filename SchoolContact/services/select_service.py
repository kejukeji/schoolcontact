# coding: UTF-8

from SchoolContact.models.students import StudentsClass
from SchoolContact.models.industry import Industry
from SchoolContact import db


def get_student_all():
    '''获取所有学生'''
    student_all = StudentsClass.query.filter().all()
    return student_all


def get_student_by_industry(industry):
    '''根据行业获取'''
    result_count = db.query(StudentsClass)\
        .join(Industry)\
    .filter(Industry.id == industry).count()