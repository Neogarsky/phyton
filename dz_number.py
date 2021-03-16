# 4 задача

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']







list_1 = ', '.join(my_list)
# print(list_1.title())  все слова с заглавной буквы
print(f'available list{my_list}')
print(f'Hello,{list_1.title()[19:25]}\n',
    f'Hello,{list_1.title()[45:51]}\n',
    f'Hello,{list_1.title()[76:83]}\n',
    f'Hello,{list_1.title()[94:100]}')


