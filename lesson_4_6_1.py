#   6. Реализовать два небольших скрипта:
#   а) итератор, генерирующий целые числа, начиная с указанного,
#   б) итератор, повторяющий элементы некоторого списка, определенного заранее
#       Подсказка: использовать функцию count() и cycle() модуля itertools.
#       Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#       Необходимо предусмотреть условие его завершения.

#
# В данной элементы списка повторяются количество раззаданное пользователем в параметрах скрипта
from itertools import cycle
import sys

if __name__ == '__main__':
    try:
        file, arg = sys.argv
        cycler = cycle(['HOP', ' ', 'HEY', ' ', 'LALALAY', ' '])
        print([next(cycler) for i in range(int(arg))])
    except ValueError:
        print('Invalid value')