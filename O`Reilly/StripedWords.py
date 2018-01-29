VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    count = 0
    sum_count = 0
    text = text.upper().replace(',',' ').replace('.',' ').replace('?',' ').split(' ')
    for i in text:
        if len(i) == 1:
            sum_count = sum_count
        else:
            for v in range(0,len(i)-1):
                if i[v] in VOWELS and i[v+1] in CONSONANTS:
                    count += 1
                elif i[v] in CONSONANTS and i[v+1] in VOWELS:
                    count += 1
            if count == (len(i)-1):
                print(i)
                sum_count += 1
                print(sum_count)
                count = 0
            else:
                count = 0
    return sum_count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("My name is ...") == 3, "All words are striped"
    # assert checkio("Hello world") == 0, "No one"
    #assert checkio("A quantity of striped words.") == 1, "Only of"
    # assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    #print('go')
    #print(checkio("My name is ..."))
    print(checkio("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?"))