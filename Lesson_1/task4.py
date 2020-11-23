
i = int(input('Введите число: '))
u = i%10
while i > 0:
    if i%10 > u:
        u = i%10
    i = i//10
print(u)
