# -*- coding: utf-8 -*-

import random
import sqlite3 as db
import collections

dbconn = db.connect('adv.sqlite')
c = dbconn.cursor()


def create_dictionary(table_name='mainseq_pl'):
    query = "SELECT * FROM {0} ORDER BY seq DESC".format(table_name)
    queryResult = c.execute(query)
    index = queryResult.fetchall()
    keys = []
    values = []
    for i in index:
        keys = keys + [i[0]]
        values = values + [i[1]]
    dictionary = collections.OrderedDict(sorted(dict(zip(keys, values)).items()))
    print(dictionary)
    return dictionary


source = create_dictionary('mainseq_pl')

html_file = open("adv.html", mode="w+")


def createAdventure():
    html_output = ""
    for dictIndex, dictCategoryName in source.items():
        query = "SELECT * FROM {0}".format(dictIndex)
        queryResult = c.execute(query)
        item = random.choice(queryResult.fetchall())
        category_name = dictCategoryName
        name = item[0]
        desc = item[1]

        print("DESC: ", desc)  # debug
        print("NAME: ", name)  # debug

        html_output = category_name + "<br><b>{0}</b>: ".format(name)
        html_output = html_output + "<br><b>Opis</b>: " + "{0}".format(desc)
        print(html_output)
        # htmlFile.write(html_output)


# html = str(createAdventure())
# print(html)
dbconn.close()
