#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        city_list = []
        for key, value in storage.all(City):
            if value.state_id == self.id:
                city_list.append(value)
        return city_list
