#!/usr/bin/python3
''' Script that prints the first State object from the database '''

from sys import argv
from sqlalchemy import create_engine, text
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Sesh = sessionmaker(bind=engine)
    sesh = Sesh()
    first_st = sesh.query(State).order_by(State.id).first()
    if first_st is not None:
        print("{}: {}".format(first_st.id, first_st.name))
    else:
        print("Nothing")
    sesh.close()
