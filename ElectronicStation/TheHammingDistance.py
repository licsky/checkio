def checkio(int1,int2):
    num = bin(int1 ^ int2).count('1')
    return num
    



if __name__ == '__main__':

    assert checkio(117, 17) == 3, "Simple"
    assert checkio(1, 2) == 2, "Simple"
    assert checkio(16, 15) == 5, "Simple"
    
    
    print(checkio(117, 17))