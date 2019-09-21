VOCABULARY = {
        'name': 'vocabulary',
        'columns': ('ID', 'hiragana', 'katakana',
                    'kanji', 'accent', 'English',
                    'Chinese'),
        'col_types': ('INTEGER PRIMARY KEY \
                      AUTOINCREMENT', 'text',
                      'text', 'text', 'int',
                      'text not NULL',
                      'text not NULL'),
        'formats': (6, 9, 9, 9, 7, 11, 10),
        'has_active': True,
        }

FIFTY = {
        'name': 'fifty',
        'columns': ('ID', 'hiragana', 'katakana',
                    'roman'),
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
        'columns': ('ID', 'hiragana', 'katakana',
                    'Chinese'),
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
    if _type.find('word') != -1:
        tableName = 'vocabulary'
    elif _type.find('character') != -1:
        tableName = 'fifty'
    elif _type.find('sentence') != -1:
        tableName = 'sentence'
    try:
        table = TABLES[tableName]
        return table
    except KeyError:
        print('Incorrect type')
        return 'ILikeAGirl'
