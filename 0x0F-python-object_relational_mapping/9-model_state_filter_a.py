#!/usr/bin/python3
""" prints all States object from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Creating a session.
    session = Session()

    # reading all State object.
    show_states = session.query(State).order_by(State.id)

    # printing from database.
    for state in show_states:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))

    # close session
    session.close()
