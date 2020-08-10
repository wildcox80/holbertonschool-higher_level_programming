#!/usr/bin/python3
'''
A script that lists all State objects that contain
the letter a from the database 'hbtn_0e_6_usa'
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Creating an instance.
    session = Session(engine)

    # reading all State object.
    all_states = session.query(State).order_by(State.id)

    # printing from database.
    for state in all_states:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))

    session.close()
