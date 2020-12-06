f_obj = open("task_1.txt", "w")
line = input('enter word\n')
f_obj.writelines(line)
while line:
    line = ('enter word\n')
    if line == '':
        break
f_obj.close()

# with open('test.txt', 'w') as f:
#     while True:
#         line = input('Р’РІРµРґРёС‚Рµ СЃС‚СЂРѕРєСѓ: ')
#         if line == '':
#             break
#         f.write(line + '\n')