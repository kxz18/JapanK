from formats.FormatPrint import printLine
from data.structure import *


def showTable(tables, cursor):
    '''in test, need to rewrite format print'''
    #loop tables(include names of tables to show)
    for tableName in tables:
        try:#get table info through its name
            table = TABLES[tableName]
        except KeyError:
            print('Table %s does not EXIST'%tableName)
            continue

        sql = 'SELECT * FROM %s;'%(tableName)
        cursor.execute(sql)
        contents = cursor.fetchall()
        printLine(table['columns'][1:],
                  table['formats'][1:],
                  divider=' ')
        for data in contents:
            printLine(data[1:], table['formats'][1:], divider=' ')
