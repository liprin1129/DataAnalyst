import sqlite3

db = sqlite3.connect("chinook.db")
c = db.cursor()

QUERY = "SELECT count(DISTINCT(Invoice.CustomerId)) as num FROM Invoice"
JOIN1 = " JOIN InvoiceLine ON Invoice.InvoiceId=InvoiceLine.InvoiceId"
JOIN2 = " JOIN Track ON InvoiceLine.TrackId=Track.TrackId"
JOIN3 = " JOIN Genre ON Track.GenreId=Genre.GenreId"
CONDITION = " WHERE Genre.Name='Jazz'"
#DISTINCT = " DISTINCT(Invoice.CustomerId)"
#GROUP = " group by Invoice.CustomerId;"

c.execute(QUERY+JOIN1+JOIN2+JOIN3+CONDITION)

result = c.fetchall()
print(result)

db.close()
