# coding: UTF-8
__author__ = 'Juingya'

from sqlalchemy import Column, Integer, String,DATETIME
from .database import Base,db

students_table = 'students'


class StudentsClass(Base):

    """
    学生信息表
    """

    __tablename__ = students_table


    id = Column(Integer, primary_key=True)
    stu_name = Column(String(50),nullable=False)
    stu_tel = Column(String(30),nullable=False)
    stu_password = Column(String(50),nullable=False)
    stu_enter_time = Column(DATETIME,nullable=True)
    stu_company = Column(String(50),nullable=True)
    stu_trade = Column(String(50),nullable=True)
    stu_position = Column(String(50),nullable=True)
    stu_contact = Column(String(50),nullable=True)


