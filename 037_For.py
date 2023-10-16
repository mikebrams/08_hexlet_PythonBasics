# def reverse_string(text):
#     # Начальное значение
#     result = ''
#     # char - переменная, в которую записывается текущий символ
#     for char in text:
#         # Соединяем в обратном порядке
#         result = char + result
#     # Цикл заканчивается, когда пройдена вся строка
#     return result
#
#
# print(reverse_string('go!'))  # => '!og'
#
#
# def chars_count(text, char):
#     # Так как ищем сумму, то начальное значение — 0
#     result = 0
#     for current_char in text:
#         # Приводим все к нижнему регистру,
#         # чтобы не зависеть от текущего регистра
#         if current_char.lower() == char.lower():
#             result += 1
#     return result
#
#
# chars_count('hexlet!', 'e')  # 2
# chars_count('hExlet!', 'e')  # 2
# chars_count('hExlet!', 'E')  # 2
#
# chars_count('hexlet!', 'a')  # 0
#
#
# def reverse_to_lower(text):
#     for char in text[::-1]:
#         print(char.lower())
#
# reverse_to_lower('HELLO')


def filter_string(text, char):
    new_text = ''

    for i in text:
        if i.lower() != char.lower():
            new_text += i

    return new_text.strip()

print(filter_string('If I look forward I win', 'i'))  # 'f  look forward  wn'
print(filter_string('If I look forward I win', 'O'))  # 'If I lk frward I win'



def is_palindrome(text):

    if not text:
        return 'True пустая строка тоже считается палиндромом'
    elif text == text[::-1]:
        return True

    return False

print(is_palindrome(''))
print(is_palindrome('radar'))
print(is_palindrome('a'))
print(is_palindrome('abs'))
print(is_palindrome('ишак ищет у тещи каши'))


def count_vowels(text):
    count = 0
    for i in text:
        if i.lower() in "aeiuoyаеёиоуыэюя":
            count += 1

    return count


print(count_vowels('London is the capital of Great Britain'))

