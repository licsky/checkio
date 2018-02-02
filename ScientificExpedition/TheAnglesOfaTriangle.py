from math import acos
from math import pi

def checkio(a, b, c):
    l = [a, b, c]
    l.sort()
    if l[0] + l[1] <= l[2]:
        return [0, 0, 0]
    angle_c = (a**2 + b**2 -c**2) / float(2 * a * b)
    angle_b = (a**2 + c**2 -b**2) / float(2 * a * c)
    angle_a = (c**2 + b**2 -a**2) / float(2 * c * b)

    ang_a = round(acos(angle_a) / pi * 180)
    ang_b = round(acos(angle_b) / pi * 180)
    ang_c = round(acos(angle_c) / pi * 180)
    result = [ang_a,ang_b,ang_c]
    result.sort()
    return result


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    # assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    # assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

    print(checkio(5,4,3))