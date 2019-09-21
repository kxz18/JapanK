
def myPrint(target, width, _end='\n', hideOverLen=False):
    '''special format print for non-English
    first decide the size of the string, then judge the overlength(if hideOverLen is true) and decide what to return'''
    size = 0
    target = str(target)
    #decide size of target
    flag = 0 #the position of the last character within width
    for i in target:
        if ord(i) >= 32 and ord(i) <= 126:
            size += 1
        else:
            size += 2
        if size <= width:
            flag += 1

    #judge if to hide over-length part
    if hideOverLen and size > width:
        leftOver = target[flag:]
        target = target[0:flag]
    else:
        leftOver = ''

    #add spaces
    while width-size > 0:
        target += ' '
        size += 1
    print(target, end=_end)
    return leftOver

def printLine(info, formats, _end='\n', autoWrap = True, divider=''):
    '''print a line conformed to formats, when auto Wrap is True, the function will print over-width part in a new line. the divider space will be added after each word'''
    #make a copy
    info = list(info)
    formats = list(formats)
    #print, if the word is completely printed, make its position an empty string, else ready to print leftover in the next line
    while info.count('') != len(info):
        for i in range(len(info)):
            info[i] = myPrint(info[i], formats[i], '', autoWrap)
            print(divider, end='')
        print('', end=_end)
