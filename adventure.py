# coding=utf-8

import random
import sqlite3 as db

#conn = db.connect('adventures.sqlite')
#c = conn.cursor()

'''
def createDictionary(tableName):
    query = "SELECT * FROM {0}".format(tableName)
    queryResult = c.execute(query)
    index = queryResult.fetchall()
    for i in index:
        source = dict("{0}".format(i[1])="{1}".format(i[2]))
        print(source)

def createAdventure():
    for dictIndex in source:
        query = "SELECT * FROM {0}".format(dictIndex)
        queryResult = c.execute(query)
        item = random.choice(queryResult.fetchall())
        name = item[0]
        desc = item[1]
        htmlOutput = "<b>{0}</b>: ".format(source[dictIndex]) + name
        htmlOutput = htmlOutput + "<br><b>Opis</b>: " + "{0}".format(desc) + ""


    # htmlFile = open("adv.html", encoding="utf-8", mode="r+")
    # htmlFile.write(htmlOutput)
'''

print("Zażółciła gęślą jaźń")
#conn.close()