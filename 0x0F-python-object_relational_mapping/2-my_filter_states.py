#!/usr/bin/python3
''' Script that takes arguments and displays all values in States '''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    rec = cur.fetchall()
    for x in rec:
        if x[1] == argv[4]:
            print(x)
    cur.close()
    db.close()
