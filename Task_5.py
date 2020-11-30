from functools import reduce

def my_func(el_1, el_n):
    return el_1 * el_n

print(f'Список четных значений - {[el for el in range (100, 1000) if el % 2 == 0]}')
print(f'Результат произведения - {reduce (my_func, [el for el in range (100, 1000) if el % 2 == 0])}')