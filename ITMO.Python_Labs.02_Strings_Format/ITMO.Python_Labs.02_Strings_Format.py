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
print(n1 + " plus " + n2 + " = ", "{:7.5f}".format(n1, n2, n3))
print('')
