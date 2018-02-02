def longest_palindromic(text):
    textr = ''.join(reversed(text))
    result = []
    a = ''
    #print(textr)
    for i in range(len(text)+1):
        for j in range(len(text)+1):
            if text[i:j] in textr and text[i:j] != '':
                result.append(text[i:j])
    for e in result:
        if len(e) > len(a):
            a = e
    return a
    

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"

    #print(longest_palindromic("artrartrt"))