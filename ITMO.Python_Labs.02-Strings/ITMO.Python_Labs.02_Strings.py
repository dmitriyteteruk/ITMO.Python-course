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
