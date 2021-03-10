a = float(input("Введите число: "))
operation = str(input("Выберете дейтсвие(+, -, *, /, //, %, **): "))
b = float(input("Введите число: "))
if operation == "+" :
    print(a + b)
elif operation == "-" :
    print(a - b)
elif operation == "*" :
    print(a * b)
elif operation == "/" :
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print(a / b)
elif operation == "//" :
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print(a // b)
elif operation == "%" :
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print(a % b)
elif operation == "**" :
    print(a ** b)
else :
    print("Выбрано неправильное действие")
