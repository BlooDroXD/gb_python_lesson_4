#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import sys

def salary(hours,price,prem):
    return (hours*price) + prem

if __name__ == '__main__':
    try:
        file, hours, price, prem = sys.argv
        print(salary(int(hours), int(price), int(prem)))
    except ValueError:
        print('Invalid value')