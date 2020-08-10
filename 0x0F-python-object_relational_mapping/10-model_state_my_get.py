#!/usr/bin/python3
'''
A script that prints the State object with the name
passed as argument from the database 'hbtn_0e_6_usa'.
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    name = sys.argv[4]
    found = False

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Creating a configured "Session" class.
    Session = sessionmaker(bind=engine)

    # create a Session.
    session = Session()

    # reading all State object.
    all_states = session.query(State)

    # printing from database (if found).
    for state in all_states:
        if state.name == name:
            print("{}".format(state.id))
            found = True
            break

    # printing message not found.
    if found is False:
            print("Not found")

session.close()
