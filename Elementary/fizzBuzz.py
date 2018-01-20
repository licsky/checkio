def checkio(number):
    if number%5 == 0 and number%3 == 0:
        number = "Fizz Buzz"
    elif number%5 == 0:
        number = "Buzz"
    elif number%3 == 0:
        number = "Fizz"
    else:
        number = str(number)
    return number

#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

    # print(checkio(15))
    # print(checkio(6))
    # print(checkio(5))
    # print(checkio(7))