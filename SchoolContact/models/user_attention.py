# coding: UTF-8

from sqlalchemy import Column, Integer, ForeignKey
from .database import Base
from .students import StudentsClass

ATTENTIONS = 'user_attention'

class Attention(Base):
    '''关注用户'''
    __tablename__ = ATTENTIONS
    id = Column(Integer, primary_key=True)
    followers = Column(Integer, ForeignKey(StudentsClass.id, ondelete='cascade', onupdate='cascade'))
    is_concerned = Column(Integer, ForeignKey(StudentsClass.id, ondelete='cascade', onupdate='cascade'))
