def timecount(s, c):
    s1 = s.split(':')
    c1 = c.split(':')
    end = []
    for i in range(0, 3):
        end.append(s1[i] + c1[i])
    hours = 0
    minutes = 0
    seconds = 0
    seconds += end[2]
    if seconds >= 60:
        seconds = seconds - 60
        minutes += 1
    minutes += end[1]
    if minutes >= 60:
        minutes = minutes - 60
        hours += 1
    hours += end[0]
    if hours >= 24:
        hours = hours - 24
    answer = f'{hours}:{minutes}:{seconds}'
    return answer


s = ''