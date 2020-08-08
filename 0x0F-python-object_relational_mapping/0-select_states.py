#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

from sys import argv
import MySQLdb


if __name__ == "__main__":

    # declaring arguments passed.
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

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
    c.execute('SELECT * FROM states ORDER BY id ASC')

    # Fetching data
    for rows in c.fetchall():
        print(rows)

    # Close cursor
    c.close()

    # Close connection database
    db.close()
