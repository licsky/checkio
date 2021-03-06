def checkio(number):
    text = '98765432'
    l = []
    for i in text:
        while number % int(i) == 0:
            l.append(i)
            number //= int(i)
    # print(l)
    # print(number)
    # print(int(''.join(reversed(l))))
    if number == 1:
        return int(''.join(reversed(l)))
    else:
        return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"

    #print(checkio(3125))
