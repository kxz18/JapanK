'''help information'''
from formats.FormatPrint import *

def __help__():
    info = [
        ('create [entry type] entry [word info]', 'create a word entry'),
        ('show [table name]', 'show the whole vocabulary'),
        ('update [table_name] SET [column1=value,...] where [some_column=some_value](use \'\' for texts)', 'update information'),
        ('recite [types] [options]', 'start random word recite'),
        ('delete [word] from [table]', 'delete an entry'),
        ('quit(exit)', 'quit'),
        ]
    print('')
    for i in info:
        printLine(i, [26, 25], divider='  ')
        print('') #use an empty line to divide item vertically
