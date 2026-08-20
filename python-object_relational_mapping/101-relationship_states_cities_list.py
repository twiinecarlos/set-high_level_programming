#!/usr/bin/python3
"""Lists states and their related cities using one query."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker
from relationship_city import City
from relationship_state import Base, State
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
 states = (
 session.query(State)
 .options(joinedload(State.cities))
 .order_by(State.id.asc())
 .all()
 )
 for state in states:
 print("{}: {}".format(state.id, state.name))
 for city in sorted(state.cities, key=lambda city: city.id):
 print("\t{}: {}".format(city.id, city.name))
 session.close()
