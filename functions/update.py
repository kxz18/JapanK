def updateInfo(command, cursor):
    try:
        cursor.execute(' '.join(command))
    except sqlite3.OperationalError as e:
        print(str(e))
    else:
        print('Successfully updated!')
