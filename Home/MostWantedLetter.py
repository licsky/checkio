def checkio(text):
    #replace this for solution
    #将数据源的中大写字母转成小写
    text = text.lower()
    l = []
    d = {}
    #循环过滤标点符号
    for i in text:
        if 97 <= ord(i) and ord(i) <=122:
            l.append(i)
    #循环统计每个字母出现的次数，装入字典
    for i in l:
        a = l.count(i)
        d[i] = a
    #定义两个标识
    temp = 1
    index = 1
    key = ''
    #按照次数大小排序,并将字典捉对组入
    d = sorted(d.items(), key=lambda x:x[0])
    print(d)
    #循环判断大小，准备输出
    for v in d:
        if index == 1:
            temp = v[1]
            index = index + 1
        if v[1] > temp:
            temp = v[1]
    for v in d:
        if v[1] == temp:
            key = v[0]
            break
    return key


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
    print(checkio('aaabb!!!!'))