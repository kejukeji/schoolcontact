# coding: UTF-8

from schoolcontact.models.database import Base, engine
from schoolcontact.models.objects import ObjectsClass
from schoolcontact.models.students import StudentsClass
from schoolcontact.models.create import CreateClass
from schoolcontact.models.interest import InterestClass



if __name__ == '__main__':
    Base.metadata.create_all(engine)