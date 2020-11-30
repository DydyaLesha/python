my_list = [9, 9, 18, 36, 72, 1, 1, 1, 144, 288]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)