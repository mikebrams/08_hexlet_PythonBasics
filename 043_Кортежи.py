def div_mod(a, b):
    quotient = a // b
    modulo = a % b
    return quotient, modulo

div_mod(13, 4)  # (3, 1)

# Как разделить значения из кортежа

name_and_age = ('Bob', 42)

(name, age) = name_and_age
print(name)  # 'Bob'
print(age)   # 42

# Кортежи и множественное присваивание

(a, b, c) = (1, 2, 3)

# Кортежи как аргументы функций


def print_person_info(person):
    name, age = person # разбираем переданный кортеж
    print(f'{name} is {age} years old')


person_tuple = ('John', 30)
print_person_info(person_tuple)  # => John is 30 years old

def sort_pair(c):
    a, b = c
    return min(a, b), max(a, b)

print(sort_pair((5, 1)))
# print(sort_pair((2, 2)))
# print(sort_pair((7, 8)))

