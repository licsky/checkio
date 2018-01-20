def long_repeat(line):
    l=[]
    count = 0
    max_count = 0
    line = line.lower()
    if line == '':
        return 0
    else:
        for i in range(len(line) - 1):
            print(line[i], line[i+1])
            if line[i] == line[i+1]:
                count = count + 1
            else:
                max_count = max(max_count, count + 1)
                count = 0
        return max(max_count, count + 1)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')

    # print(long_repeat(''))