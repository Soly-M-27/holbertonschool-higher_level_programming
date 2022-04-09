#!/usr/bin/python3
''' Script to lists states from database table '''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rec = cur.fetchall()
    for x in rec:
        if x[1][0] == 'N':
            print(x)
    cur.close()
    db.close()
