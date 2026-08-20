#!/usr/bin/python3
"""Lists all City objects and their related State objects."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import configure_mappers, joinedload, sessionmaker

from relationship_city import City
from relationship_state import State


if __name__ == "__main__":
    configure_mappers()

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
        session.query(City)
        .options(joinedload(City.state))
        .order_by(City.id.asc())
        .all()
    )

    for city in cities:
        print("{}: {} -> {}".format(
            city.id,
            city.name,
            city.state.name
        ))

    session.close()
