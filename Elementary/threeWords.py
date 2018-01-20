def checkio(words):
    l = words.lower().split(' ')
    count = 0
    flag = True
    print(l)
    for i in l:
        print(i)
        if i.islower() == True:
            count += 1
        elif count >=3:
            break
        else:
            count = 0
    print(count)
    if count >=  3:
        pass
    else:
        flag = False
    return flag

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("Hello World hello") == True, "Hello"
    # assert checkio("He is 123 man") == False, "123 man"
    # assert checkio("1 2 3 4") == False, "Digits"
    # assert checkio("bla bla bla bla") == True, "Bla Bla"
    # assert checkio("Hi") == False, "Hi"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))