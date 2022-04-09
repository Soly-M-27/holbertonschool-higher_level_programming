#!/usr/bin/python3
''' Prints all City objects from the database '''

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine, orm
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    sesh = orm.sessionmaker(bind=engine)()
    ct = sesh.query(State.name, City.id, City.name).filter(
         City.state_id == State.id).order_by(City.id)
    for city in ct:
        print("{}: ({}) {}".format(*city))
    session.close()
