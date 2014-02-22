# coding: UTF-8
__author__ = 'Juingya'

from .database import Base,db
from sqlalchemy import Column,Integer,ForeignKey
from .students import *
from .objects import *


create_table = 'create'

class CreateClass(Base):
    """
              创建项目映射表
    """
    __tablename__ = create_table

    id = Column(Integer,primary_key=True)
    stu_id = Column(Integer,ForeignKey(StudentsClass.id,ondelete='cascade', onupdate='cascade'), nullable=False)
    obj_id = Column(Integer,ForeignKey(ObjectsClass.id,ondelete='cascade',onupdate='cascade'),nullable=False)




