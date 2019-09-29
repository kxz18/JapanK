import sqlite3
from data.structure import TABLES
from core.display import myPrint, printLine, __help__
from core.function import showTable, recite, search
from core.operation import createEntry, createTable, updateInfo, delete

def interaction():
    db = sqlite3.connect('./data/japanese.db')
    cursor = db.cursor()
    initialize(cursor) #initialize database
    db.commit()

    #declaration
    print('Developed by KXZ, powered by python')
    print('You can enter "help" for help')

    #get commands
    lastCmd = ''
    while True:
        command = input('japanK> ').split(" ")
        for i in range(len(command)):#to lower case
            command[i] = command[i].lower()
        try:
            if command[0] == '/':
                if lastCmd != '':
                    command = lastCmd
                else:
                    print("No previous command!")
                    continue
            if command[0] == 'quit' or command[0] == 'exit':
                break
            elif command[0] == 'help':
                __help__()
            elif command[0] == 'create':
                if command[2] ==  'entry':
                    createEntry(command[1], command[3:], cursor)
            elif command[0] == 'show':
                showTable(command[1:], cursor)
            elif command[0] == 'recite':
                recite(command[1], cursor, command[2:])
            elif command[0] == 'update':
                updateInfo(command, cursor)
            elif command[0] == 'search':
                search(command[1:], cursor)
            elif command[0] == 'delete':
                delete(command[1:], cursor)
            else:
                print('Invalid command!')
            lastCmd = command
            db.commit()
        except IndexError:
            print('missing arguments')

    print('Remember me forever~Bye~')
    db.close()

def getTables(cursor):
    #get all table names
    sql = 'SELECT name from sqlite_master WHERE type="table" order by name'
    cursor.execute(sql)
    results = cursor.fetchall()
    results = [x[0] for x in results]
    return results

def initialize(cursor):
    results = getTables(cursor)
    #create new tables
    for name in TABLES:
        if name not in results:
            createTable(TABLES[name], cursor)
            

    

if __name__ == '__main__':
    interaction()
