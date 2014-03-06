# coding: UTF-8

from SchoolContact.models.students import StudentsClass as Student
from SchoolContact.models.industry import Industry
from SchoolContact import db
from sqlalchemy import or_,and_

def get_student_all():
    '''获取所有学生'''
    student_all = Student.query.filter().all()
    return student_all


def get_student_by_industry(industry):
    '''根据行业获取'''
    result_count = db.query(Student)\
        .join(Industry)\
    .filter(Industry.id == industry).count()


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

def vague_count(para):
    #模糊查询

    para_int = int(para)
    student_count = Student.query.filter(or_(Student.stu_name.like('%'+para+'%'),Student.stu_enter_time.like('%'+para+'%'),Student.industry_id.like('%'+para_int+'%'),Student.stu_company.like('%'+para+'%'),Student.stu_position.like('%'+para+'%'))).count()
    return student_count

def vague_first(para):
    #查询到一个
     para_int = int(para)
     student_first =Student.query.filter(or_(Student.stu_name.like('%'+para+'%'),Student.stu_enter_time.like('%'+para+'%'),Student.industry_id.like('%'+para_int+'%'),Student.stu_company.like('%'+para+'%'),Student.stu_position.like('%'+para+'%'))).first()
     return student_first
def vague_all(para):
     #查询到多条
     para_int = int(para)
     student_all =Student.query.filter(or_(Student.stu_name.like('%'+para+'%'),Student.stu_enter_time.like('%'+para+'%'),Student.industry_id.like('%'+para_int+'%'),Student.stu_company.like('%'+para+'%'),Student.stu_position.like('%'+para+'%'))).all()
     return student_all