# Аннотации типов — это возможность указать типы параметров и
# возвращаемого значения у функции в Python

def concat(first, second):
    return first + second


def concat2(first: str, second: str) -> str:
    return first + second

# Аннотации типов также могут быть использованы для определения
# типов переменных внутри функции.

def double(n: int) -> int:
    result: int = n * 2
    return result


def letter_multiply(text: str, symbol: str, num: int) -> str:
    return text.replace(symbol, symbol * num)


print(letter_multiply('python', 'n', 4))


def get_age_difference(a, b):
    return f'The age difference is {abs(b - a)}'


print(get_age_difference(2001, 2018))


a = "asdf"
a = a.replace("a", "u")
b = a
print(a, b)

print(id(a))
print(id(b))
