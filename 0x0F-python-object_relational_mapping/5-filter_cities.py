#!/usr/bin/python3
''' Script to list all cities from State as argument '''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states\
                ON cities.state_id=states.id AND states.name=%s\
                ORDER BY cities.id ASC", (argv[4]))
    rec = cur.fetchall()
    print(", ".join(x[0] for x in rec))
    cur.close()
    db.close()
