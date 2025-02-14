#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__= 'places'

    """city_id and user_id missing Foreign Key relationship"""
    city_id = Column(String(60), nullable=False)

    user_id = Column(String(60), nullable=False)

    name = Column(String(128), nullable=False)

    description = Column(String(1024), nullable=False)

    number_rooms = Column(Integer, nullable=False, default=0)

    number_bathrooms = Column(Integer, nullable=False, default=0)

    max_guest = Column(Integer, nullable=False, default=0)

    price_by_night = Column(Integer, nullable=False, default=0)

    latitude = Column(Float, nullable=False)

    longitude = Column(Float, nullable=False)

    amenity_ids = []
