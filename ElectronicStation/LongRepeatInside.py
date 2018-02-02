def repeat_inside(line):
    #抄的
    ans = ''
    suffixes = []
    temp = ''
    for i in range(len(line)):
        suffixes.append(line[i:])
    for suf in suffixes:
        for j in range(len(suf)):
            temp = temp + suf[j]
            x = suf.count(temp)
            y = x*temp
            if (x>=2) & (len(y)>len(ans)) & (y in suf):
                ans = x*temp
                
        temp = ''
    
    return ans



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')

    #repeat_inside('abcabcabab')