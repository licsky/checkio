def long_repeat(line):
    for i in line:
        print(i)
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert long_repeat('sdsffffse') == 4, "First"
    # assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    # print('"Run" is good. How is "Check"?')

    long_repeat('sdsffffse')