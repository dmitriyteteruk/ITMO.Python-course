# Алгоритм 4. Обработка статической последовательности данных известной длины

print('Введите длину последовательности n: ')

n = int(input())
while n > 0:
    S = 0
    for i in range(1, n + 1):
        S += int(input("Введите любое число: "))
    print("Mid ", S / i)
    break;

