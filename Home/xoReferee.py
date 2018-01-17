def checkio(game_result):
    flag = ''
    game1 = zip(*game_result)
    if game_result[0][0] == game_result[1][1] ==game_result[2][2] and game_result[0][0] != '.':
        flag = game_result[0][0]
    elif game_result[0][2] == game_result[1][1] ==game_result[2][0] and game_result[0][2] != '.':
        flag = game_result[0][2]
    else:
        flag = 'D'
    for i in game_result:
        if i[0] == i[1] == i[2] and i[0] != ".":
            flag = i[0]
    for i in game1:
        if i[0] == i[1] == i[2] and i[0] != ".":
            flag = i[0]
    for i in game_result:
        if i == '.':
            flag = 'D'
    return flag

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

