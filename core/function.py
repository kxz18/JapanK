#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
from core.display import myPrint, printLine
from data.structure import *

def recite(_type, cursor, additional=[]):
    '''recite function, first judge which table to
    refer to by _type, then randomly choose from
    the active list of the table to recite'''

    table = toTable(_type)
    if table == 'ILikeAGirl':#related table not found
        return
    sql = 'SELECT * FROM active_%s;'%(table['name'])
    cursor.execute(sql)
    IDs = [x[0] for x in cursor.fetchall()]
    if not IDs:
        print('No active {}'.format(_type))
        return
    
    operation = ''
    while operation != '0':
        cur = random.randint(0, len(IDs)-1)
        sql = 'SELECT * from {} where ID={};'.format(table['name'], IDs[cur])
        del IDs[cur]#delete recited words
        cursor.execute(sql)
        wordInfo = cursor.fetchall()[0]
        print('')#start new line
        if (table['name'] == 'fifty' and 'katakana' in additional) or str(wordInfo[1]) == '':#required to show katakana or hiragana is null
            myPrint(wordInfo[2], 10)
        else:
            myPrint(wordInfo[1], 10)
        print('')
        input('press Enter to see defination: ')
        print('')
        printLine(table['columns'][1:], table['formats'][1:], divider=' ')
        printLine(wordInfo[1:], table['formats'][1:], divider=' ')
        print('')
        operation = input('press Enter to continue,"d" to deactive this word, "0" to quit:')
        if operation == 'd':
            sql = "DELETE FROM active_{} where ID={};".format(table['name'], int(wordInfo[0]))
            cursor.execute(sql)
            print('deactived')
        if not IDs:#pylint suggest using not IDs  instead of len(IDs)==0 to judge if it is empty
            print('All have been recited')
            break

def showTable(tables, cursor):
    '''show the contents of the selected tables'''
    #loop tables(include names of tables to show)
    for tableName in tables:
        try:#get table info through its name
            table = toTable(tableName)#TABLES[tableName]
        except KeyError:
            print('Table %s does not EXIST'%tableName)
            continue

        sql = 'SELECT * FROM %s;'%(table['name'])
        cursor.execute(sql)
        contents = cursor.fetchall()
        printLine(table['columns'][1:],
                  table['formats'][1:],
                  divider=' ')
        for data in contents:
            printLine(data[1:], table['formats'][1:], divider=' ')
