def popular_words(text, words):
    dict = {}
    l=[]
    count = 0
    for i in range(1,len(words)+1):
        l.append('count_' + str(i))
    text = text.lower().replace(',', ' ').replace('.',' ').replace('\n',' ').split(' ')
    for v in range(0,len(words)):
        for i in text:
            if words[v] == i:
                count += 1
        dict[words[v]] = count
        count = 0
    return dict


if __name__ == '__main__':
#     print(popular_words('''
# When I was One,
# I had just begun.
# When I was Two,
# I was nearly new.
# ''', ['i', 'was', 'three']))
    print(popular_words('''It's flying from somewhere\nAs fast as it can,\nI couldn't keep up with it,\nNot if I ran.''',["it's","ran"]))
    # These "asserts" are used for self-checking and not for an auto-testing
#     assert popular_words('''
# When I was One,
# I had just begun.
# When I was Two,
# I was nearly new.
# ''', ['i', 'was', 'three']) == {
#         'i': 4,
#         'was': 3,
#         'three': 0
#     }
#     print("Coding complete? Click 'Check' to earn cool rewards!")

