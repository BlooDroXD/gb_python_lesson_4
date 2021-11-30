#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from itertools import count
from math import factorial
def fact(n):
    for n in count(1):
        yield factorial(n)

if __name__ == '__main__':
    try:
        lines = []
        x=0
        n = int(input())
        lines.append(f'{n}! = ')
        for el in fact(n):
            if x < n:
                if x != 0:
                    lines.append(''.join(f'{x}'))
                    x += 1
                    lines.append(''.join(' * '))
                else:
                    x += 1
                if x == n:
                    lines.append(''.join(f'{x} = {el}'))
                    x += 1
            else:
                break
        print(''.join(lines))
    except ValueError:
        print('Invalid value')
