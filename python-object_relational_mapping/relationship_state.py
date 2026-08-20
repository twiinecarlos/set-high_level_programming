#!/usr/bin/python3
"""Defines the State class and its cities relationship."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from relationship_city import Base, City


class State(Base):
    """Represents a State in the states table."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete"
    )
