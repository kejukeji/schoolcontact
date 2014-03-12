# coding: UTF-8
__author__ = 'Juingya'

from sqlalchemy import Column, Integer, String,DATETIME, ForeignKey
from .database import Base,db
from .industry import Industry
from .base_class import *

students_table = 'students'


class StudentsClass(Base, InitUpdate):

    """
    学生信息表
    """

    __tablename__ = students_table


    id = Column(Integer, primary_key=True)
    stu_name = Column(String(50),nullable=False)
    stu_tel = Column(String(30),nullable=True)
    stu_password = Column(String(50),nullable=False)
    stu_enter_time = Column(DATETIME,nullable=True)
    stu_company = Column(String(50),nullable=True)
    industry_id = Column(Integer, ForeignKey(Industry.id, ondelete='cascade', onupdate='cascade'))
    stu_position = Column(String(50),nullable=True)
    stu_contact = Column(String(50),nullable=True)
    openid = Column(String(100), nullable=True)
    avatar_img_url = Column(String(500), nullable=True)
    account_qq = Column(String(20), nullable=True)
    account_wechat = Column(String(20), nullable=True)

    def update(self,**kwargs):
        '''修改'''
        self.update_value(('stu_name','stu_tel','stu_enter_time','stu_company','industry_id','stu_position'
                           ,'stu_contact','account_qq', 'account_wechat'), kwargs)


