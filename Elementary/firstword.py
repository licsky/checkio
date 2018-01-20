def first_word(text: str) -> str:
    text = text.replace(',',' ')
    text = text.replace('.',' ')
    l = text.split(' ')
    word = ''
    #print(l)
    for i in l:
        #print(len(i))
        try:
            if len(i) > 0:
                #print(i)
                word = i
                break
        except TypeError:
            pass
    #print(word)
    return word



if __name__ == '__main__':
    # print("Example:")
    # print(first_word(" a word "))
    # print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")

