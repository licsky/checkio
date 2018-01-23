def is_stressful(subj):
    flag = False
    count = 0 
    sub = ''
    if subj.isupper() is True:
        flag = True
    for i in subj:
        if i.isalpha() is True:
            if len(sub) == 0:
                sub += i
            elif i != sub[-1]:
                sub += i
    sub = sub.lower()
    print(sub)
    if 'help' in sub:
        flag = True
    if 'asap' in sub:
        flag = True
    if 'urgent' in sub:
        flag = True
    if subj[-1] == subj[-2] == subj[-3] == '!':
        flag = True
    return flag


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert is_stressful("Hi") == False, "First"
    # assert is_stressful("I neeed HELP") == True, "Second"
    # print('Done! Go Check it!')

    print(is_stressful("We need you A.S.A.P.!!"))
    print(is_stressful("UUUURGGGEEEEENT here"))
    print(is_stressful("Heeeeeey!!! I\u2019m having so much fun!\u201d"))
    

