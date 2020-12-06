# out_f = open("task_2.txt", "r")
# content = out_f.read()
# print (len(content))
# out_f.close()

out_f = open("task_2.txt", "r")

for line in out_f:
    print (len(line))
out_f.close()