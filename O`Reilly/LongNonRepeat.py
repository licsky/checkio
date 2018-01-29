def non_repeat(line):
    max_text = ''
    if len(line) <= 1:
        max_text = line
    else:
        for e in range(len(line)):
            start = e
            text = line[e]
            for i in range(start,len(line)-1):     
                if line[i] != line[i+1] and line[i+1] not in text:
                    text += line[i+1]
                else:
                    start = i+1
                    if len(text) > len(max_text):
                        max_text = text
                    text = line[i+1]
            if len(max_text) < len(text):
                max_text = text
    return max_text

if __name__ == '__main__':
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert non_repeat('aaaaa') == 'a', "First"
    # assert non_repeat('abdjwawk') == 'abdjw', "Second"
    # assert non_repeat('abcabcffab') == 'abcf', "Third"
    # print('"Run" is good. How is "Check"?')

    print(non_repeat('wq'))
    print(non_repeat('abdjwawk'))

    print(non_repeat("fghfrtyfgh"))