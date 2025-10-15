#1)
a = int(input("введите первое число: "))
b = int(input("введите второе число: "))
c = int(input("введите третье число: "))
print("выберите операцию: ")
print("1 - сумма трёх чисел: ")
print("2 - произведение ваших чисел: ")
qw = input("ваш выбор: 1 или 2: ")
if qw == "1":
    result = a + b + c
    print(f"сумма ваших чисел: {result}")
elif qw == "2":
    result = a * b * c
    print(f"произведение ваших чисел: {result}")
else:
    print("ошибка, выберите 1,2")

#2)
num1 = int(input("введите первое число: "))
num2 = int(input('введите второе число: '))
num3 = int(input('введите третье число: '))
print("выберите операцию:")
print("1 - максимум из трех")
print("2 - минимум из трех")
print("3 - среднее арифметическое")
qw = input("ваш выбор 1, 2, 3: ")
if qw == "1":
    result = max(num1, num2, num3)
    print(f"максимальное число: {result}")
elif qw ==  "2":
    result = min(num1, num2, num3)
    print(f"минимальное число: {result}")
elif qw == "3":
    result = (num1 + num2 + num3) / 3
    print(f"среднее арифметическое: {result}")
else:
    print('ошибка, выбери 1,2,3')

#задание 3
mil = 0.000621371
duim = 39.3701
yard = 1.09361
n = int(input("введите количество метров: "))
print("выберите операцию: ")
print("1 - перевести в мили: ")
print("2 - перевести в дюймы: ")
print("3 - перевести в ярды: ")
n1 = input("ваш выбор: 1, 2, 3")
if n1 == "1":
    result = n * mil
    print(f"метры в милях:{result}")
elif n1 == "2":
    result = n * duim
    print(f"метры в дюймах:{result}")
elif n1 == "3":
    result = n * yard
    print(f"метры в ярдах:{result}")
else:
    print('ошибка, выбери 1,2,3')









