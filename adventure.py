import random
import sqlite3 as db

conn = db.connect('adventures.sqlite')
c = conn.cursor()

result = c.execute("SELECT * from THEMES")

theme = random.choice(result.fetchall())

print(theme[1], ':', theme[2])
