

from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as f_a:
    with open('bakery.csv', encoding='utf-8') as f_r:
        if len(argv) == 1:  # проверяем введено значение
            print(f_r.read())
        elif len(argv) == 2:
            if ',' in argv[1]:
                f_r.read()
                print(argv[1], file=f_a)
            # выводим на экран начиная с 1
            else:
                print(*f_r.readlines()[int(argv[1]) - 1:], sep='')
        else:
            print(*f_r.read().split()[int(argv[1]):int(argv[2]) + 1], sep='\n')
