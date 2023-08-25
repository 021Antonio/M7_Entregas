#Tabela de user_bases

from sqlalchemy import Column, Integer,String, Float
from model.base import Base

class UserBase(Base):
    __tablename__ = 'user_base'
    id = Column(Integer, primary_key= True,autoincrement= 'auto')
    name = Column(String)
    password = Column(String)

    def __init__(self, name, password):
        self.name = name
        self.password = password
   

    def __repr__(self):
        return f'UserBase {self}'
