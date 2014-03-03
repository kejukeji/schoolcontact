# coding: UTF-8

from SchoolContact.models.database import Base, engine
from SchoolContact.models.objects import ObjectsClass
from SchoolContact.models.students import StudentsClass
from SchoolContact.models.create import CreateClass
from SchoolContact.models.interest import InterestClass
from SchoolContact.models.industry import Industry
from SchoolContact.models.user_attention import Attention



if __name__ == '__main__':
    Base.metadata.create_all(engine)