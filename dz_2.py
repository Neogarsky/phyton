
list_set = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(list_set)):
    if not list_set[i].isalpha():
        list_set[i] = f'{int(list_set[i]):02}'

        if '+' in list_set[i]:
            list_set[i] = f'+{int(list_set[i]):02}'
        elif '-' in list_set[i]:
            list_set[i] = f'{int(list_set[i]):03}'
            print(list_set[i])

my_string = " ".join(list_set)
my_string_2 = my_string.replace(' "  ', ' " ')
my_string_3 = my_string_2.replace('  " ', ' " ')
print(my_string)
