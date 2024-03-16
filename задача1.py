import csv


def timecount(s, c):
    """
    Описание функции timecount.

    функция просчитывает конечное время с учётом того,
    что в сутках 24 часа

    Описание аргументов:
    s – строка вида 'hh:mm:ss' - время в момент остановки
    с – строка, одно число - время простоя в часах
    """

    s1 = s.split(':')
    hours = int(s1[0])
    hours += int(c)
    if hours >= 24:
        hours = hours - 24
    if hours < 10:
        hours = '0' + str(hours)
    return f'{hours}:{s1[1]}:{s1[2]}'


with open('astronaut_time.csv', encoding='utf8') as f:
    data = csv.DictReader(f, delimiter=',')
    with open('new_time.txt', 'w', encoding='utf8') as txtfile:
        for row in data:
            txtfile.write(
                f'На станции {row['numberStation']} в каюте {row['cabinNumber']}'
                f' восстановлено время. Актуальное время: {timecount(row['timeStop'], row['count'])}\n')

with open('new_time.txt', encoding='utf8') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
