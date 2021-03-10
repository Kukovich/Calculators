name = input("Введите имя: ")

print("Привет" , name)

print("Сложение")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print(a + b)

print("Вычитание")
c = float(input("Введите первое число: "))
d = float(input("Введите второе число: "))
print(c - d)

print("Умножение")
e = float(input("Введите первое число: "))
f = float(input("Введите второе число: "))
print(e * f)

print("Деление")
g = float(input("Введите первое число: "))
h = float(input("Введите второе число: "))
if h == 0:
    print("На ноль делить нельзя")
else:
    print(g / h)

print("Целочислительное деление")
i = float(input("Введите первое число: "))
j = float(input("Введите второе число: "))
if j == 0:
    print("На ноль делить нельзя")
else:
    print(i // j)

print("Остаток от деления")
k = float(input("Введите первое число: "))
l = float(input("Введите второе число: "))
if l == 0:
    print("На ноль делить нельзя")
else:
    print(k % l)

print("Возведение в степень")
m = float(input("Введите первое число: "))
n = float(input("Введите второе число: "))
print(m ** n)

name1 = a + b
name2 = c - d
name3 = e * f
if h == 0:
    name4 = "На ноль делить нельзя"
else:
    name4 = g / h
if j == 0:
    name5 = "На ноль делить нельзя"
else:
    name5 = i // j
if l == 0:
    name6 = "На ноль делить нельзя"
else:
    name6 = k % l
name7 = m ** n

print("Результат сложения =", name1)
print("Результат вычитания =", name2)
print("Результат умножения =", name3)
print("Результат деления =", name4)
print("Результат целочислительного деления =", name5)
print("Остаток от деления =", name6)
print("Результат возведения в степень =", name7)