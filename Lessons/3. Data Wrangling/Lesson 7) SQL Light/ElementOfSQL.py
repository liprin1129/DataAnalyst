import sqlite3

connection = sqlite3.connect('chinook.db')

with connection:

    cursor = connection.cursor()
    for row in cursor.execute("SELECT Name FROM Track WHERE Composer='AC/DC'"):
        print(row)
    #connection.execute("SELECT Name FROM Track WHERE Composer='AC/DC'")
    #connection.execute(".tables")

    #connection.close()
