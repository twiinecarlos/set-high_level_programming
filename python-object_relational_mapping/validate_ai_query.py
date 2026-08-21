#!/usr/bin/python3
"""Validates the corrected SQLAlchemy ORM query."""

from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker

from setup_db import City


def validate_ai_query(username=None, password=None, db_name=None):
    """Execute the corrected ORM query and print City/State data."""
    engine = create_engine("sqlite:///orm_practice.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
        session.query(City)
        .options(joinedload(City.state))
        .order_by(City.id.asc())
        .all()
    )

    for city in cities:
        print("{}: {} from {}".format(
            city.id,
            city.name,
            city.state.name
        ))

    session.close()


if __name__ == "__main__":
    validate_ai_query()
