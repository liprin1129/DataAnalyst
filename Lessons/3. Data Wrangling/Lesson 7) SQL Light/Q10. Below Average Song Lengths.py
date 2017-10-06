import sqlite3

db = sqlite3.connect("chinook.db")
c = db.cursor()

SELECT = "SELECT Genre.Name, count(*) as genre_count "
FROM = "FROM Track "
JOIN = "JOIN Genre ON Track.GenreId=Genre.GenreId, "
SUBQUERY = "(SELECT avg(milliseconds) as songs_avg FROM Track) "
WHERE = "WHERE Track.milliseconds<songs_avg "
GROUP_BY = "group by Genre.Name "
ORDER_BY = "order by genre_count desc "
LIMIT = "limit 1;"

c.execute(SELECT+FROM+JOIN+SUBQUERY+WHERE+GROUP_BY+ORDER_BY+LIMIT)

result = c.fetchall()
print(result[0])

db.close()
