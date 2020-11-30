from itertools import count

for el in count(int(input('Введите стартовое число'))):
    if el > 15:
        break
    else:
        print(el)

from itertools import cycle
count = 1
my_list = ['vvv', True, 2.81, 7, None]

for el in cycle(my_list):
    if count > 6:
        break
    print(my_list)
    count += 1