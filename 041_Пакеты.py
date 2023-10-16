
'''Пакеты — группы модулей'''

# Пакет — это каталог (директория) с файлами модулей, имеющий имя в формате
# snake_case и содержащий специальный модуль с именем «__init__.py».
# Именно наличие этого специального файла подсказывает интерпретатору Python,
# что каталог следует воспринимать как пакет.

import package

print(package.NAME)

# Как импортировать пакеты

import package.functions
import package.constants

package.functions.greet(package.constants.PERSON)

# Попробуем импортировать отдельные определения, то есть саму функцию и аргумент:

from package.functions import greet
from package.constants import PERSON

greet(PERSON)


# !!!!!!!! Кроме того, импорты в Python бывают двух видов:

# Абсолютный импорт
# В абсолютном импорте нужно прописывать полный путь до модуля, включающего
# все пакеты и подпакеты. Полные пути гарантируют простоту чтения и однозначность
# — так всем будет понятно, что и откуда импортируется.

# Относительный импорт
# Относительные импорты выглядят так:

from . import module
from .module import function
from .subpackage.module import CONSTANT



