import sqlite3 as db

conn = db.connect('adventures.sqlite')
c = conn.cursor()

source = {"themes": "Głowny temat", "villains": "Przeciwnik", "minor_villains": "Pomocnik")}

for tableName[0] in source:
    query = "SELECT * FROM {0}".format(tableName[0])
# debug
queryResult = c.execute(query)
tableName = random.choice(queryResult.fetchall())
print(tableName[0])
