#!/usr/bin/python3
""" displays lists all cities from the database hbtn_0e_4_usa """

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
    c.execute("SELECT cities.name FROM states INNER JOIN cities ON states.id\
    = cities.state_id WHERE states.name=%s ORDER BY cities.id ASC")
    query_rows = c.fetchall()

    # Fetching data
    print(", ".join([row[0] for row in query_rows]))

    # Close cursor
    c.close()

    # Close connection database
    db.close()
