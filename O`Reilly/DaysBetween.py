from datetime import date, timedelta

def days_diff(date1, date2):
    #通过date函数将日期转化
    f = date(date1[0],date1[1],date1[2])
    #s = date(date2[0],date2[1],date2[2])
    s = date(*date2)
    a = abs((f-s).days)
    return a

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # days_diff((1982, 4, 19), (1982, 4, 22))
    # days_diff((2014, 1, 1), (2014, 8, 27))
    # days_diff((2014, 8, 27), (2014, 1, 1))
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
