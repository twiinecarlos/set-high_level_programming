#!/usr/bin/python3
"""Defines the City class and its State relationship."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from relationship_state import Base


class City(Base):
    """Represents a City stored in the cities table."""

    __tablename__ = "cities"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )

    state = relationship(
        "State",
        back_populates="cities"
    )
