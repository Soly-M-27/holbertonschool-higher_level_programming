#!/usr/bin/python3
''' List all objects from database '''

import sys
from sys import argv
from sqlalchemy import create_engine, text
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Sesh = sessionmaker(bind=engine)
    sesh = Sesh()
    rec = sesh.query(State).order_by(State.id)
    for x in rec:
        print("{}: {}".format(x.id, x.name))
