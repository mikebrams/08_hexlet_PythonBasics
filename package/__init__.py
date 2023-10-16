NAME = 'super_package'

from package.functions import greet
from package.names import NAME

# BEGIN (write your solution here)

GREETING = greet(NAME)
print(GREETING)
# END

# Добавьте в __init__.py константу GREETING, которая должна содержать
# результат применения функции greet() к константе NAME.
# И функция и константа импортируются из модулей пакета
# в блоке импортов модуля __init__.py.

