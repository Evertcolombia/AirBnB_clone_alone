#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from modesl.city import City
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        """ return the current relation ship between state and city
            for filestorage"""
        name = ""
        @property
        def cities(self):
            from models.storage import storage
            city_list = []
            cities = storage.all(City)
            for el in cities.values():
                if el.state_id == self.id:
                    city_list.append(el)
            return city_list
            


