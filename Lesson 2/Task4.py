# my_str = input("дверь асфальтоукладчик азулежу")
# my_word = []
# num = 1
# for el in range(my_str.count('') + 1):
#     my_word = my_str.split()
#     if len(str(my_word)) <= 10:
#         print(f"{num} {my_word[el]}")
#         num += 1
#     else:
#         print(f"{num} {my_word[el][0:10]}")
#         num += 1
my_str = input(" Введите слово")
my_word = ["дверь асфальтоукладчик азулежу"]
#my_word = str(my_str)
#my_str = str(my_word)
num = 1
my_str = my_str.lstrip()
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word[el])) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1