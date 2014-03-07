# coding: UTF-8

from sqlalchemy import Column, Integer, ForeignKey
from .database import Base
from .students import StudentsClass
from .base_class import *

ATTENTIONS = 'user_attention'

class Attention(Base, InitUpdate):
    '''关注用户'''
    __tablename__ = ATTENTIONS
    id = Column(Integer, primary_key=True)
    followers = Column(Integer, ForeignKey(StudentsClass.id, ondelete='cascade', onupdate='cascade'))
    is_concerned = Column(Integer, ForeignKey(StudentsClass.id, ondelete='cascade', onupdate='cascade'))

    def __init__(self, **kwargs):
        '''初始化'''
        args = ('followers', 'is_concerned')
        self.init_value(args, kwargs)
