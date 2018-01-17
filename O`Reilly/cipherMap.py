def recall_password(cipher_grille, ciphered_password):
    x = cipher_grille
    y = ciphered_password
    temp = 0
    l = ''
    for o in range(4):
        for i in range(4):
            for u in range(4):
                if x[i][u] == 'X':
                    l = l + (y[i][u])
        x = list(zip(*x[::-1]))
    return l
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
