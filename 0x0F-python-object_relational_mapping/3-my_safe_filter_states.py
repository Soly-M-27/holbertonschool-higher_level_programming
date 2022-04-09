#!/usr/bin/python3
''' Script to be safe from SQL injections '''

from email import charset
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (argv[4]))
    rec = cur.fetchall()
    for x in rec:
        print(x)
    cur.close()
    db.close()
