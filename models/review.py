#!/usr/bin/python3
""" Module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column,String,ForeignKey

class Review(BaseModel):
    """ Review class to store review information """
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)

