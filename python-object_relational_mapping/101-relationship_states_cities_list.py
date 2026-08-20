#!/usr/bin/python3
"""Lists all State objects and their related City objects."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import State


if __name__ == "__main__":
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

    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

        cities = sorted(state.cities, key=lambda city: city.id)

        for city in cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
