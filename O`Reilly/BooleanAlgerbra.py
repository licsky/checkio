OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    flag = 1
    if operation == 'conjunction':
        if x == y == 1:
            pass
        else:
            flag = 0
    if operation == 'disjunction':
        if x == y == 0:
            flag = 0
        else:
            pass
    if operation == 'implication':
        if x == 1:
            flag = y
        else:
            pass
    if operation == 'exclusive':
        if x == y:
            flag = 0
        else:
            pass
    if operation == 'equivalence':
        if x == y:
            pass
        else:
            flag = 0
    return flag

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

