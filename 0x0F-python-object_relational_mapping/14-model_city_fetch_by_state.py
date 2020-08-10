#!/usr/bin/python3
""" class definition of a City """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Creating a configured "Session" class.
    Session = sessionmaker(bind=engine)

    # create a Session.
    session = Session()

    # defining a query:
    query = session.query(City, State) \
                   .filter(City.state_id == State.id) \
                   .order_by(City.id)

    # printing according to the format.
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
