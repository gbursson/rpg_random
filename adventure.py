# -*- coding: utf-8 -*-

import random
import sqlite3 as db
import collections

dbconn = db.connect('adv.sqlite')
c = dbconn.cursor()

def createDictionary(tableName='mainseq_pl'):
    query = "SELECT * FROM {0} ORDER BY seq DESC".format(tableName)
    queryResult = c.execute(query)
    index = queryResult.fetchall()
    keys = []
    values = []
    for i in index:
        keys = keys + [i[0]]
        values = values + [i[1]]
    dictionary = dict(zip(keys, values))
    dictionary = collections.OrderedDict(sorted(dictionary.items()))
    return dictionary

source = createDictionary('mainseq_pl')

def createAdventure():
    for dictIndex, dictCategoryName in source.items():
        query = "SELECT * FROM {0}".format(dictIndex)
        queryResult = c.execute(query)
        item = random.choice(queryResult.fetchall())
        category_name = dictCategoryName
        name = item[0]
        desc = item[1]
        htmlOutput = category_name + "<br><b>{0}</b>: ".format(name)
        htmlOutput = htmlOutput + "<br><b>Opis</b>: " + "{0}".format(desc)
        print(htmlOutput)

htmlFile = open("adv.html", mode="w+")
html = str(createAdventure())
#print(html)
htmlFile.write(html)
dbconn.close()