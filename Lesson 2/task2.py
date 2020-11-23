num_count = int(input("Введите количество элементов списка "))
my_list = []
q = 0
num = 0
while q < num_count:
    my_list.append(input("Введите следующее значение списка"))
    q += 1
for a in range(int(len(my_list)/2)):
    my_list[num], my_list[num+1] = my_list[num+1], my_list[num]
    num += 2
print(my_list)