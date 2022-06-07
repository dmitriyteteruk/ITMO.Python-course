# Лабораторная 2
# Работа со строками
# Задача 1 
print("##### Работа со строками #####")
print("----- Задача 01 -----")
string1 = " This is a string. "
print(string1)
string2 = " This is another string. "
print(string2)
print('')

print("----- Задача 02 -----")
# Задача 2
a = string1 + string2
print(a)
print('')

# Задача 3
print("----- Задача 03 -----")
print(len(string1))
print(string1.title())
print(string1.lower())
print(string1.upper())
print(string1.rstrip())
print(string1.lstrip())
print(string1.strip())
print(string1.strip('0'))
print('')

# Задача 4
print("----- Задача 04 -----")
string3 = string1[6]
print(string3)
print('')

# Задача 5
print("----- Задача 05 -----")
string3 = string1[1:8]
print('')

# Задача 6
print("----- Задача 06 -----")
print(string3)
string3 = string1[3:]
print(string3)
string3 = string1[:8]
print(string3)
string3 = string1[1:3:8]
print(string3)

# Задача 6
# print("----- Задача 07 -----")
# string1[3] = '0'
# print(string1)

print('')

# Работа с числами
print("##### Работа с числами #####")
# Задача 1
print("----- Задача 01, 02 -----")
a = int(5)
b = int(17)
c = int(a/b)
print("Операция деления целого числа 5 на 17")
print(c)

d = int(b/a)
print("Операция деления целого числа 17 на 5")
print(d)

e = int(b%a)
print("Операция взятия остатка целого числа 5 от 17")
print(e)

f = int(a%b)
print("Операция взятия остатка целого числа 17 от 5")
print(f)

g = int(a ** b)
print("Операция возведения числа 5 в степень 5")
print(g)
print('')

print("----- Задача 03 -----")
param = "string" + str(15)
print(param)
print('')

# Преобразование данных
print("##### Преобразование данных #####")
# Задача 1
print("----- Задача 01 -----")
param2 = "string " + str(15)
print(param2)
print('')

# Задача 2
print("----- Задача 02 -----")
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)
print('')

# Форматирование строк
print("##### Форматирование строк #####")
# Задача 2
print("----- Задача 02 -----")
a = 1/3
print("{:7.3f}".format(a))
print('')

# Задача 3
print("----- Задача 03 -----")
a = 2/3
b = 2/9
print("{:7.6f} {:7.6f}".format(a, b))
print("{:10.6e} {:10.6e}".format(a, b))
print('')

# Задача 4
print("----- Задача 04 -----")
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", "{:7.5f}".format(n3))
print('')
