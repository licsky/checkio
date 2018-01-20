def checkio(array):
    count = 0
    try:
        for i in range(0,len(array)):
            if i % 2 == 0:
                count = count + array[i]
        count = count * array[-1]
    except IndexError :
        pass
    return count
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    # assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    # assert checkio([6]) == 36, "(6)*6=36"
    # assert checkio([]) == 0, "An empty array = 0"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    print(checkio([-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]))