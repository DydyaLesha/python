def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        arg2 + arg3
print(f'result - {my_func(int(input("arg1")), int(input("arg2")), int(input("arg3")))}')
