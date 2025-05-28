#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
      __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

     if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref="state"
                               cascade="all, delete, delete-orphan")
    else:
        @property
         def cities(self):
                 """Get a list of all related City objects."""
            city_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
