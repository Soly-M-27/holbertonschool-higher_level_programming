#!/usr/bin/python3
''' List all objects from database '''

from sys import argv
from sqlalchemy import create_engine, text
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
Sesh = sessionmaker(bind=engine)
sesh = Sesh()
rec = sesh.query(State.id, State.name).from_statement(text(
    "SELECT id, name "
    "FROM states "
    "ORDER BY states.id ASC "
    )).all()
for id, name in rec:
    print("{:d}: {:s}".format(id, name))
    sesh.close()
