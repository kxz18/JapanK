from formats.FormatPrint import *

def delete(parameters, cursor):
    #still in test
    try:
        fromIndex = parameters.index('from')
        tableName = parameters[fromIndex+1]
        sql  = 'SELECT name from sqlite_master WHERE type="table" order by name'
        cursor.execute(sql)
        results = cursor.fetchall()
        results = [x[0] for x in results]
        if tableName not in results:
            raise KeyError
    except (ValueError, IndexError):
        print('You forget to designate table name!')
        return
    except KeyError:
        print("Wrong table name")
        return
    
    for i in range(0,fromIndex+1):
        sql = "SELECT * FROM {} where hiragana='{}' or katakana='{}' or kanji='{}';".format(tableName,parameters[i],parameters[i],parameters[i])
        cursor.execute(sql)
        matched = cursor.fetchall()
        for single in matched:
            printLine(single[1:], vocabulary_formats[1:], divider=' ')
            confirm = input('Enter 1 to confirm deletion: ')
            if confirm == '1':
                sql = 'DELETE FROM {} where ID={}'.format(tableName, int(single[0]))
                cursor.execute(sql)
                sql = 'DELETE FROM active_{} where ID={}'.format(tableName, int(single[0]))
                cursor.execute(sql)
                print('deleted')
            else:
                print('cancelled')
