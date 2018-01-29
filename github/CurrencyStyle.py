def checkio(text):
    text = text.split(' ')
    result = []
    for i in text:
        if i.startswith('$'):
            if i.endswith('.') or i.endswith(','):
                a = i[:-4].replace('.',',')
                b = i[-4:-1].replace(',','.',1)
                c = i[-1]
                new_word = a + b + c
            else:
                a = i[:-3].replace('.',',')
                b = i[-3:-1].replace(',','.',1)
                c = i[-1]
                new_word = a + b + c
            result.append(new_word)
        else:
            result.append(i)
    return ' '.join(result)



if __name__ == '__main__':    

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
    assert checkio("$0,89") == "$0.89" , "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9", "Dollars without cents"

    #print(checkio("$1.234.567,89"))
