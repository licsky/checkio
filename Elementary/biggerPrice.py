def bigger_price(limit, data):
    l=[]
    li = []
    for k in range(1,limit+1):
        for i in data:
            l.append(i['price'])
        max_num = max(l)
        l = []
        for i in data:
            for v in i.items():
                if max_num in v:
                    li.append(i)
                    data.remove(i)
                    
    return li


if __name__ == '__main__':
    from pprint import pprint
    # pprint(bigger_price(2, [
    #     {"name": "bread", "price": 100},
    #     {"name": "wine", "price": 138},
    #     {"name": "meat", "price": 15},
    #     {"name": "water", "price": 1}
    # ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')

