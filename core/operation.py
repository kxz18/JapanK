#!/usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3
from core.display import printLine
from data.structure import *

def createEntry(kind, inList, cursor):
    '''create new entry according to different type'''
    if kind.find('word') != -1:
        table = VOCABULARY
    elif kind.find('character') != -1:
        table = FIFTY
    #input data should not include ID which automatically increase
    if len(inList) != len(table['columns'])-1:
        inList.clear()
        for column in table['columns'][1:]:
            inList.append(input("%s: "%(column)))
    #link columns and values for sql
    columns = ''
    values = ''
    for _name, _type, _value in zip(table['columns'][1:], table['col_types'][1:], inList):
        columns += '%s,'%(_name)
        if _type.lower().find('text') != -1:
            values += "'%s',"%(_value)
        else:
            values += '%s,'%(_value)
    #add new word
    try:
        sql = 'INSERT INTO %s (%s) VALUES (%s);'%(table['name'],columns[0:-1],values[0:-1])
        cursor.execute(sql)
        sql = 'SELECT last_insert_rowid() from %s;'%(table['name'])
        cursor.execute(sql)
        id = cursor.fetchone()
        sql = 'INSERT INTO active_%s (ID) VALUES (%d)'%(table['name'], id[0])
        cursor.execute(sql)
        cursor.fetchall()#clear answer list
        print('(%s) has been added'%(values[0:-1]))
    except sqlite3.OperationalError as e:
        print(str(e))

def createTable(table, cursor):
    #link columns and their types
    columns = ''
    for column in zip(table['columns'], table['col_types']):
        columns += (' ').join(column)+','

    sql = 'CREATE TABLE {} ({});'.format(table['name'], columns[0:-1])#avoid the last comma
    cursor.execute(sql)
    #judge if it has active affiliation
    if table['has_active']:
        sql = 'CREATE TABLE active_{} (ID int PRIMARY KEY not NULL);'.format(table['name'])
    cursor.execute(sql)
    sql = '''SELECT ID from {} ORDER by ID;'''.format(table['name'])

def updateInfo(command, cursor):
    try:
        cursor.execute(' '.join(command))
    except sqlite3.OperationalError as e:
        print(str(e))
    else:
        print('Successfully updated!')

def delete(parameters, cursor):
    #still in test
    try:
        fromIndex = parameters.index('from')
        tableName = parameters[fromIndex+1]
        table  = toTable(tableName)
    except (ValueError, IndexError):
        print('You forget to designate table name!')
        return
    except KeyError:
        print("Wrong table name")
        return
    #start deleting, parameters after 'from' are all items designated to be deleted
    for i in range(0,fromIndex+1):
        searchContent = ''
        for index in table['searchIndex']:
            searchContent += "%s='%s' or "%(index, parameters[i])
        #delete the last 'or'
        searchContent = searchContent[0:-4]

        sql = "SELECT * FROM {} where {};".format(tableName,searchContent)
        cursor.execute(sql)
        matched = cursor.fetchall()
        for single in matched:
            printLine(single[1:], table['formats'][1:], divider=' ')
            confirm = input('Enter 1 to confirm deletion: ')
            if confirm == '1':
                sql = 'DELETE FROM {} where ID={}'.format(tableName, int(single[0]))
                cursor.execute(sql)
                sql = 'DELETE FROM active_{} where ID={}'.format(tableName, int(single[0]))
                cursor.execute(sql)
                print('deleted')
            else:
                print('cancelled')
