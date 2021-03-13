duration = [53, 153, 4153, 400153]


for el in range(len(duration)):
    if duration[el] < 60:
        s = duration[el] % 60

        print('duration =', duration[el])
        print(s, 'сек')
    elif duration[el] < 3600 >= 60:
        s = duration[el] % 60
        m = (duration[el] - (duration[el] // 3600) * 3600) // 60
        print('duration =', duration[el])
        print(m, 'мин', s, 'сек')
    elif duration[el] < 86400:
        s = duration[el] % 60
        m = (duration[el] - (duration[el] // 3600) * 3600) // 60
        h = duration[el] // 3600
        print('duration =', duration[el])
        print(h, 'час', m, 'мин', s, 'сек')
    elif duration[el] >= 86400:
            d = duration[el] // 86400
            s = duration[el] % 60
            m = (duration[el] - (duration[el] // 3600) * 3600) // 60
            h = duration[el] // 3600 // 60
            print('duration =', duration[el])
            print(d, 'дн', h, 'час', m, 'мин', s, 'сек')