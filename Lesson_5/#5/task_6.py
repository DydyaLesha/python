# subj = {}
# with open('task_6.txt', encoding='utf-8') as f:
#     for line in f:
#         subject, lecture, practice, lab = line.split()
#         subj[subject] = int(lecture(lecture.find('('))) + int(practice(practice.find('('))) + int(lab(lab.find('(')))
#     print(f'Общее количество часов по предмету - \n {subj}')

my_dict = dict()
with open('task_6.txt') as f:
     lines = f.readlines()

for line in lines:
    splitted_line = line.split()
    subject = splitted_line[0]
    sum_lessons = sum([int(x[:x.find('(')])for x in splitted_line[1:] if '(' in x])
    my_dict[subject[:-1]] = sum_lessons
print(my_dict)