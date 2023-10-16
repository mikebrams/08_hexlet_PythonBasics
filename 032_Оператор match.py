status = ""

    # if status == 'processing':
    #     # Делаем раз
    # elif status == 'paid':
    #     # Делаем два
    # elif status == 'new':
    #     # Делаем три
    # else:
    #     # Делаем четыре


# Оператор match позволяет записать этот код короче и выразительнее:

# match status:
#     case 'processing':  # status == 'processing'
#         # Делаем раз
#     case 'paid':  # status == 'paid'
#         # Делаем два
#     case 'new':  # status == 'new'
#         # Делаем три
#     case _:  # else
#         # Делаем четыре

# А вот внутри каждого case ситуация другая.
# Здесь можно выполнять любой произвольный код:

# match count:
#     case 1:
#         # Делаем что-то полезное
#     case 2:
#         # Делаем что-то полезное
#     case _:
#         # Что-то делаем

# Два способа вернуть результат

# Создать переменную перед match, заполнить ее в case и затем
# в конце вернуть значение этой переменной наружу:

    # def count_items(count):
    #     # Объявляем переменную
    #     result = ''
    #
    #     # Заполняем
    #     match count:
    #         case 1:
    #             result = 'one'
    #         case 2:
    #             result = 'two'
    #         case _:
    #             result = None
    #
    #     # Возвращаем
    #     return result

# или

# def count_items(count):
#     match count:
#         case 1:
#             return 'one'
#         case 2:
#             return 'two'
#         case _:
#             return None


# Несколько значений в case
# С помощью оператора | (или) можно объединять несколько значений в один case,
# чтобы выполнять одну и ту же операцию ветвления. Например:

# def match_input(input):
#     match input:
#         case 'start' | 'begin':
#             print('Starting...')
#         case 'stop' | 'end':
#             print('Stopping...')
#         case 'pause':
#             print('Pausing...')
#         case _:
#             print('Invalid input')
#
# match_input('begin')  # => Starting...
# match_input('stop')  # => Stopping...
# match_input('pause')  # => Pausing...
# match_input('test')  # => Invalid input

# Проверка типов
# В операторе case можно использовать функции приведения типов, например,
# str(), int(). Это нужно, чтобы проверять тип переменной после match:

# def get_type(val):
#     match val:
#         case str(val):
#             print(f'It is a string: {val}')
#         case int(val):
#             print(f'It is an integer: {val}')
#         case _:
#             print("I don't know this type")
#
# get_type('hello')  # => It is a string: hello
# get_type(123)  # => It is an integer: 123
# get_type(None)  # => I don't know this type

# Определение переменной в case
# Если определить переменную после case, то ей будет присвоено значение,
# которое связано с соответствием с match:

# def match_input(input):
#     match input:
#         case 'start':
#             message = 'Starting...'
#         case 'stop':
#             message = 'Stopping...'
#         case 'pause':
#             message = 'Pausing...'
#         case _:
#             message = 'Invalid input'
#
#     print(message)
#
# match_input('start')  # => Starting...
# match_input('stop')  # => Stopping...
# match_input('pause')  # => Pausing...
# match_input('test')  # => Invalid input

# Здесь обязательно нужно задать дефолтный случай — _. Так как если ни один
# case не соответствует входному значению, переменная message не будет
# определена. Это вызовет ошибку NameError.

def get_number_explanation(num):
    match num:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'





