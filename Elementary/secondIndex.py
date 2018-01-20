def second_index(text: str, symbol: str):
    count = text.find(symbol)
    if text.find(symbol, count+1) == -1:
        return None
    else:
        return text.find(symbol, count+1)


if __name__ == '__main__':
    
    #print(second_index("sim s", " "))

    #These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')

