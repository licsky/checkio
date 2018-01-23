def most_frequent(data):
    num = 0
    d ={}
    for i in data:
        num = data.count(i)
        a = i
        d[i] = num
    return sorted(d.items(),key=lambda x: x[1],reverse=True)[0][0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert most_frequent([
    #     'a', 'b', 'c', 
    #     'a', 'b',
    #     'a'
    # ]) == 'a'

    # assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    # print('Done')

    # print(most_frequent([
    #     'a', 'b', 'c', 
    #     'a', 'b',
    #     'a'
    # ]))