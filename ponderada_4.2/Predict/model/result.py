from sqlalchemy import Column, Integer,String, Float
from model.base import Base_predict

class UserBase(Base):
    __tablename__ = 'user_base'
    id = Column(Integer, primary_key= True,autoincrement= 'auto')
    result_predict = Column(float)

    def __init__(self, name, password):
        self.result_predict = result_predict
        
   

    def __repr__(self):
        return f'UserBase {self}'