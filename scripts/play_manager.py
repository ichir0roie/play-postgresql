# https://docs.sqlalchemy.org/en/14/

from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()


class Table1(Base):
    __tablename__ = "table1"
    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)
    column3 = Column(String)
    
    
class Table2(Base):
    __tablename__ = "table2"
    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)
    column3 = Column(String)
    