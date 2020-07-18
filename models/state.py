#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """ State class """
    if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='states')
    else:
        name = ""
    
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if os.environ.get("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            city_list = []
            cities = models.storage.all(City)
            for el in cities.values():
                if el.state_id == self.id:
                    city_list.append(el)
            return city_list
