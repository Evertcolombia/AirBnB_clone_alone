#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, ForeignKey, Float, Integer, String, Table
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    place_amenity = Table('place_amenity', Base.metadata,
            Column('place_id',
                String(60),
                ForeignKey('places.id'),
                primary_key=True,
                nullable=False),
            Column('amienity_id',
                String(60),
                ForeignKey('amenities.id'),
                primary_key=True,
                nullable=False))


    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship("Amenity",
                secondary=place_amenity,
                back_populates="place_amenities",
                viewonly=False)
    else:
        """
        It will be the FileStorage relationship between
        Place and Review
        """
        from models.storage import storage

        @property
        def reviews(self):
            from models.review import Review
            reviews_list = []
            objects = storage.all(Review)
                
            for el in objects.values():
                if el.place_id == self.id:
                    reviews_list.append(el)
            return reviews_list

        @property
        def amenities(self):
            amenities_list = []
            objects = storage.all()

            for el in objects:
               if el.place_id == self.id and obj.__class__.__name__ == 'Amenity':
                   reviews_list.append(el)
            return reviews_list
        
        @amenities.setter
        def amenities(self, cls):
            if cls.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(cls.amenities.id)

