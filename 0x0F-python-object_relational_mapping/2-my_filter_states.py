#!/usr/bin/python3
""" lists all states with a name starting with N """

from sys import argv
import MySQLdb


if __name__ == "__main__":

    # declaring arguments passed.
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]

    # Connecting to MySQL database

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    # Making cursor
    c = db.cursor()

    # Executing query
    "SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id\
    ASC".format(argv[4])
    query_rows = c.fetchall()

    # Fetching data
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)

    # Close cursor
    c.close()

    # Close connection database
    db.close()
