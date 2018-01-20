def checkio(*args):
    if not args:
        result = 0
    else:
        l = list(args)
        max_num = max(l)
        min_num = min(l)
        result = max_num - min_num
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

    # print(checkio())
    # print(checkio(5, -5))
    # print(checkio(10.2, -2.2, 0, 1.1, 0.5))