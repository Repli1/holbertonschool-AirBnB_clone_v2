#!/usr/bin/pythoD3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, ForeignKey, Integer, String

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states_id'), nullable=False)
