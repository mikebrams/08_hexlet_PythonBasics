def print_params(a, b=2, c=None, d=4):
    print(a, b, c, d)

# Нужно передать только d, но приходится передавать все
print_params(1, 2, None, 8)

# Именованные аргументы позволяют передавать только d
# Для остальных аргументов используются значения по умолчанию
a = 1
print_params(2, d=8)


def trim_and_repeat(text, offset=0, repetitions=1):
    return text[offset:] * repetitions


print(trim_and_repeat('python', offset=3, repetitions=2))
