#!/usr/bin/python3
'''
A script that adds the State object “Louisiana”
to the database 'hbtn_0e_6_usa'.
'''

import sys
from model_state import Base, State
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

    # adding Louisiana state.
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    # printing from database (if found).
    print(louisiana.id)

    session.close()
