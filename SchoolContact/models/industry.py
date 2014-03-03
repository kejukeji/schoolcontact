# coding: UTF-8

from .database import Base
from sqlalchemy import Column, String, Integer

INDUSTRY = 'industry'

class Industry(Base):
    '''行业'''
    __tablename__ = INDUSTRY
    id = Column(Integer, primary_key=True)
    industry_name = Column(String(20), nullable=False)
