import sqlite3

db = sqlite3.connect("chinook.db")
c = db.cursor()

QUERY = "SELECT count(*) FROM Track JOIN Genre ON Track.GenreId=Genre.GenreId JOIN MediaType ON Track.MediaTypeId=MediaType.MediaTypeId WHERE Genre.Name='Pop' and MediaType.Name='MPEG audio file';"

c.execute(QUERY)

result = c.fetchall()

print(result)
