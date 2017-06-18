# coding=utf-8

#import random
import sqlite3 as db
import collections


dbconn = db.connect('adv.sqlite')
c = dbconn.cursor()


def createDictionary(tableName):
    query = "SELECT * FROM {0} ORDER BY seq DESC".format(tableName)
    queryResult = c.execute(query)
    index = queryResult.fetchall()
    keys = []
    values = []
    for i in index:
        keys = keys + [i[0]]
        values = values + [i[1]]
    source = dict(zip(keys, values))
    source = collections.OrderedDict(sorted(source.items()))
    print(source) #debug

#createDictionary("mainseq_pl")

'''
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



#conn.close()