def divmode():
    try:
        arg1 = int(input("Введите делимое "))
        arg2 = int(input("Введите делитель "))
        rem = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return rem
print(f'результат {divmode()}')
