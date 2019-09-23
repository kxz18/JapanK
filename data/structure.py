'''data structrue, you can add your own table here:
    name: name of table, columns: column names, searchIndex: column used to search,
    col_types: data types of each column, formats: width of each column when printed,
    has_active: if it has an active list affiliation(used to recite)
    WARNING: the first column should always be 'ID' which automatically increases'''
VOCABULARY = {
        'name': 'vocabulary',
        'columns': ('ID', 'hiragana', 'katakana',
                    'kanji', 'accent', 'English',
                    'Chinese'),
        'searchIndex': ('hiragana', 'katakana', 'kanji'),
        'col_types': ('INTEGER PRIMARY KEY \
                      AUTOINCREMENT', 'text',
                      'text', 'text', 'int',
                      'text not NULL',
                      'text not NULL'),
        'formats': (6, 10, 9, 9, 7, 12, 10),
        'has_active': True,
        }

FIFTY = {
        'name': 'fifty',
        'columns': ('ID', 'hiragana', 'katakana',
                    'roman'),
        'searchIndex': ('hiragana', 'katakana', 'roman'),
        'col_types': ('INTEGER PRIMARY KEY \
                      AUTOINCREMENT',
                      'text not NULL',
                      'text not NULL',
                      'text not NULL'),
        'formats': (6, 8, 8, 5),
        'has_active': True,
        }

SENTENCE = {
        'name': 'sentence',
        'columns': ('ID', 'kanji', 'katakana',
                    'Chinese'),
        'searchIndex': ('kanji', 'katakana'),
        'col_types': ('INTEGER PRIMARY KEY \
                      AUTOINCREMENT',
                      'text not NULL',
                      'text not NULL',
                      'text not NULL'),
        'formats': (6, 25, 25, 25),
        'has_active': True
        }

TABLES = {
        'vocabulary': VOCABULARY,
        'fifty': FIFTY,
        'sentence': SENTENCE
        }

def toTable(_type):
    '''from input get the required table'''
    tableName = ''
    _type = _type.lower()
    if _type.find('word') != -1 or _type.find('vocabulary') != -1:
        tableName = 'vocabulary'
    elif _type.find('character') != -1 or _type.find('fifty') != -1:
        tableName = 'fifty'
    elif _type.find('sentence') != -1:
        tableName = 'sentence'
    try:
        table = TABLES[tableName]
        return table
    except KeyError:
        raise KeyError('Incorrect type or table name')
