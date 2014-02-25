# coding: UTF-8

from SchoolContact.models.database import Base, engine
from SchoolContact.models.objects import ObjectsClass
from SchoolContact.models.students import StudentsClass
from SchoolContact.models.create import CreateClass
from SchoolContact.models.interest import InterestClass



if __name__ == '__main__':
    Base.metadata.create_all(engine)