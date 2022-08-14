from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import BOOLEAN

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Zoo(Base):
    __tablename__ = 'zoo'

    id = Column(Integer, primary_key=True)
    name_of_zoo = Column(String(50))
    name_of_animal = Column(String(50))
    family = Column(String(50))
    hungry = Column(BOOLEAN)
    age = Column(Integer)

