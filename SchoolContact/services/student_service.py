__author__ = 'Juingya'
# coding: UTF-8
from SchoolContact.models.students import StudentsClass as Student
from SchoolContact.models.database import *
from SchoolContact.models.industry import *
import hashlib
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
    else:
        return 'None'


def update(Student):
    '''修改'''
    db.commit()


def get_student_by_openId(openId):
    '''根据openid查询用户'''
    student = Student.query.filter(Student.openid == openId).first() #
    if student:
        return str(student.id)
    return str(None)

def check_student_is_none(student, temp_str):
    industry = get_industry_by_industry_id(student.industry_id) # 根据student中的industry_id得到industry
    student.industry = ''
    if industry:
        student.industry = industry.industry_name
    if student != 'None' or student != False:
        if student.stu_enter_time:
            student.stu_enter_time = str(student.stu_enter_time)[0:10]
        if student.stu_enter_time == None:
            student.stu_enter_time = temp_str
        if student.stu_company == None or student.stu_company == '':
            student.stu_company = temp_str
        if student.industry == '':
            student.industry = temp_str
        if student.stu_position == None or student.stu_position == '':
            student.stu_position = temp_str
        if student.stu_contact == None or student.stu_contact == '':
            student.stu_contact = temp_str
        if student.account_qq == None or student.account_qq == '':
            student.account_qq = temp_str
        if student.account_wechat == None or student.account_wechat == '':
            student.account_wechat = temp_str
        if student.stu_tel == None or student.stu_tel == '':
            student.stu_tel = temp_str


def insert_user(nickname, openid, headimgurl):
    '''添加授权微信用户到本app数据库中'''
    password = hashlib.new('md5', '888888').hexdigest()
    student = Student(stu_name=nickname, openid=openid, avatar_img_url=headimgurl, stu_password=password, stu_tel=18716262204) # 得到
    db.add(student)
    try:
        db.commit()
        return student
    except:
        return 'None'


def get_industry_by_industry_id(industry_id):
    '''获取student对应行业'''
    industry = Industry.query.filter(Industry.id == industry_id).first()
    if industry:
        return industry
    return None


def get_industry():
    '''获取行业全部'''
    industry_count = Industry.query.filter().count()
    if industry_count > 1:
        industry = Industry.query.filter().all()
    else:
        industry = Industry.query.filter().frist()
    return industry, industry_count
