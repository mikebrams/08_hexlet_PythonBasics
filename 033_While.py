def print_numbers(num):
    while num > 0:
        print(num)
        num -= 1
    print('finished!')


print_numbers(4)
#
#
# def count_chars(string, char):
#     index = 0
#     count = 0
#     while index < len(string):
#         if string[index] == char:
#             # Считаем только подходящие символы
#             count = count + 1
#         # Счетчик увеличивается в любом случае
#         index = index + 1
#     return count

# Представим расширенную функцию my_substr(). Она принимает три аргумента:
# строку, индекс и длину извлекаемой подстроки. Функция возвращает подстроку
# указанной длины, начиная с указанного индекса. Примеры вызова:

# Какие пограничные случаи стоит учитывать:

# - Отрицательная длина извлекаемой подстроки
# - Отрицательный заданный индекс
# - Заданный индекс выходит за границу всей строки
# - Длина подстроки в сумме с заданным индексом выходит за границу всей строки


def has_char(text, char):
    index = 0

    while index < len(text):
        if text[index].lower() == char.lower():
            return True
        index += 1

    return False

print(has_char('Hexlet', 'x'))  # => True
print(has_char('Hexlet', 'h'))  # => True
print(has_char('Awesomeness', 'd'))  # => False
