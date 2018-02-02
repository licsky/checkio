def checkio(first, second):
    first1 = first.split(',')
    second1 = second.split(',')
    result = []
    for i in first1:
        if i in second1:
            result.append(i)
    return ','.join(sorted(result))
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    # assert checkio("one,two,three", "four,five,six") == "", "Too different"
    # assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"

    print(checkio("one,two,three","four,five,one,two,six,three"))