#!/usr/bin/python3
"""Creates a SQLite database for the ORM debugging challenge."""

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()


class State(Base):
    """Represents a state."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    cities = relationship("City", back_populates="state")


class City(Base):
    """Represents a city."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    state_id = Column(Integer, ForeignKey("states.id"))
    state = relationship("State", back_populates="cities")


engine = create_engine("sqlite:///orm_practice.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if session.query(State).count() == 0:
    california = State(name="California")
    new_york = State(name="New York")

    session.add_all([california, new_york])
    session.commit()

    session.add_all([
        City(name="Los Angeles", state=california),
        City(name="San Francisco", state=california),
        City(name="New York City", state=new_york),
        City(name="Buffalo", state=new_york)
    ])
    session.commit()

session.close()
