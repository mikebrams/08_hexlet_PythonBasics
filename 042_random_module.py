# Модуль random

# randint — сгенерировать целое число в заданном диапазоне
# choice — выбрать случайный элемент из заданного набора

from random import randint

random_number = randint(1, 100)
print(random_number)

# Выбор случайного элемента

from random import choice

string = 'abcde'
char = choice(string)

# !!!!! При этом важно, чтобы строка для выбора не была пустой.
# Иначе мы получим ошибку IndexError: Cannot choose from an empty sequence:
# «Нельзя выбрать из пустой строки».

print(char)

def choice_from_range(text, st, fn):
    return text[randint(st, fn)]

print(choice_from_range("abcdef", 3, 5))