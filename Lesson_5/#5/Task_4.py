trans = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('task_4.txt', encoding='utf-8') as f:

    for i in f:
        i = i.split(' ', 1)
        new_file.append(trans[i[0]] + ' ' + i[1])
    print(new_file)

with open('task_4_new.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_file)
