# coding: utf-8
__author__ = 'Juingya'

from sqlalchemy import Column,Integer,String,DATETIME
from .database import Base

objects_table = 'objects'

class ObjectsClass(Base):
    """
    项目信息
    """

    __tablename__ = objects_table

    id = Column(Integer,primary_key = True)
    obj_name = Column(String(50),nullable=False)
    obj_description = Column(String(100),nullable=False)
    obj_s_time = Column(DATETIME,nullable=False)
    obj_e_time = Column(DATETIME,nullable=False)
    obj_state = Column(Integer,nullable=False)

