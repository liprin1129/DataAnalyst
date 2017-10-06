import sqlite3
db = sqlite3.connect('chinook.db')
c = db.cursor()
QUERY = 'SELECT * FROM Invoice;'
c.execute(QUERY)
rows = c.fetchall()

#print('Row data:', rows)

#for row in rows:
#    print('  ', row[0:])

import pandas as pd
df = pd.DataFrame(rows)

print(df)

db.close()
