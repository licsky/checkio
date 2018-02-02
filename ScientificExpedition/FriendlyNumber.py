def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    count = 0
    for i in range(len(powers)-1):
        if abs(number) >= base:
            number = round(number / base, 3)
            count += 1
    if decimals == 0:
        number = int(number)
    else:
        number = round(number, decimals)
    return '{:.{dec}f}{}{}'.format(number, powers[count], suffix, dec=decimals)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert friendly_number(102) == '102', '102'
    # assert friendly_number(10240) == '10k', '10k'
    # assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    # assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    # assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    
    #print(friendly_number(255000000000, powers=["","k","M"]))
    print(friendly_number(10**24))