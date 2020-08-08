#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa where name """

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
    c.execute("SELECT * FROM states WHERE name=%s ORDER BY id\
    ASC".format(name))
    query_rows = c.fetchall()

    # Fetching data
    for row in query_rows:
        if row[1] == name:
            print(row)

    # Close cursor
    c.close()

    # Close connection database
    db.close()
