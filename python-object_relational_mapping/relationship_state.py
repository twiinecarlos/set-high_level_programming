#!/usr/bin/python3
"""Defines the State class with a cities relationship."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class State(Base):
    """Represents the states table."""

    __tablename__ = "states"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete-orphan"
    )
