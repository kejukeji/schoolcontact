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
    industry = Industry.query.filter(Industry.id == student.industry_id).first()
    student.industry = ''
    if industry:
        student.industry = industry.industry_name
    if student != 'None' or student != False:
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
        if student.account_qq == None:
            student.account_qq = temp_str
        if student.account_wechat == None:
            student.account_wechat = temp_str


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



