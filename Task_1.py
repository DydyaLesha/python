# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
# сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# import time
# print(time.time())
#
# print('Start Game!')
# time.sleep(1)
# print('Loading world!')

# from sys import argv
#
# name, time, salary, bonus = argv
# try:
#     time = float(input('time'))
#     salary = float(input('salary'))
#     bonus = float(input('bonus'))
#     num = time * salary + bonus
#     print(f'Заработная плата сотрудника{num}')
# except ValueError:
#     print('Not a number')

from sys import argv

try:
    name, time, salary, bonus = argv[1:]
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
except ValueError:
        print('Not a number')