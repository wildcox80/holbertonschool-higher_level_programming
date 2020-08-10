#!/usr/bin/python3
"""
    Python Script to create a class City
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


# City class, that inherits from Base.

class City(Base):
    """Creates the class State"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
