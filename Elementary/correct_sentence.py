def correct_sentence(text):
    text = text.capitalize()
    if '.' not in text:
        text = text + '.'
    else:
        pass
    return text


if __name__ == '__main__':
    # print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    print("Coding complete? Click 'Check' to earn cool rewards!")

# str = "greetings, friends"
# print(str.upper())          # 把所有字符中的小写字母转换成大写字母
# print(str.lower())          # 把所有字符中的大写字母转换成小写字母
# print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
# print(str.title())