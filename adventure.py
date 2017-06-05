# -*- coding: utf-8 -*-

import random
import sqlite3 as db

conn = db.connect('adventures.sqlite')
c = conn.cursor()

source = {"themes": "Glowny temat", "villains": "Przeciwnik", "minor_villains": "Pomocnik"}

for dictIndex in source:
    query = "SELECT * FROM {0}".format(dictIndex)
    queryResult = c.execute(query)
    item = random.choice(queryResult.fetchall())
    name = item[0]
    desc = item[1]
    htmlOutput = "<b>{0}</b>: ".format(source[dictIndex]) + name
    htmlOutput = htmlOutput + "<br><b>Opis</b>: " + "{0}".format(desc) + ""
    htmlOutput = str(htmlOutput)

    print(htmlOutput)

    # htmlFile = open("adv.html", encoding="utf-8", mode="r+")
    # htmlFile.write(htmlOutput)
