with open("task_3.txt") as f_obj:
    salary = []
    lines = f_obj.readlines()
    for line in lines :
        name, sal = line.split(' - ')
        salary.append(int(sal))
        if int(sal) < 20000:
           print(line, end='')
print('\nCредняя зп:', sum(salary) / len(salary))
