from sqlalchemy import Column, Integer, String, Sequence, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Predictions(Base):
    __tablename__ = 'predictions'
    id = Column(Integer, Sequence('predict_id_seq'), primary_key=True)
    predictions = Column(float, unique=True)
    