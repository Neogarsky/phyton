num_eng_rus = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'}


def num_translate(el):
    print(num_eng_rus.setdefault(el))


num_translate("zero")
num_translate("nine")
num_translate("одинадцать")






