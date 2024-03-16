def timecount(s, c):
    s1 = s.split(':')
    hours = int(s1[0])
    hours += c
    if hours >= 24:
        hours = hours - 24
    if hours < 10:
        hours = '0' + str(hours)
    return f'{hours}:{s1[1]}:{s1[2]}'


print(timecount('04:26:47', 24))
