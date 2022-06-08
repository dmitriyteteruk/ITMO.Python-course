# Лаборатоная 4, циклы и ветвление

from random import randint
import time

# ввод имен играющих
igrok1 = input('Введите имя игрока №1: ')
igrok2 = input('Введите имя игрока №2: ')

# добавляем счетчики побед и очков
wins_counter1 = 0
wins_counter2 = 0
sum_of_points1 = 0
sum_of_points2 = 0

for i in range(5):

    # моделирование бросания кубика 1 игроком
    print('')
    print('Раунд', i+1)
    print('Кубик бросает', igrok1)
    time.sleep(1)
    n1 = randint (1, 6)
    print('Выпало число', n1)
    sum_of_points1 += n1           # суммируем очки
    print('Сумма очков игрока', igrok1, 'после попытки №', i+1, 'равна', sum_of_points1)

    # моделирование бросания кубика 2 игроком
    print('Кубик бросает', igrok2)
    time.sleep(1)
    n2 = randint (1, 6)
    print('Выпало число', n2)
    sum_of_points2 += n2           # суммируем очки
    print('Сумма очков игрока', igrok2, 'после попытки №', i+1, 'равна', sum_of_points2)

    if n1 > n2:
        wins_counter1 +=1
        print('В этом раунде выиграл', igrok1)
    elif n1 < n2:
        wins_counter2 +=1
        print('В этом раунде выиграл', igrok2)
    else:
        print('Ничья')
    

# Определение победителя
if wins_counter1 > wins_counter2:
    print('')
    print('Победил', igrok1)
    print('Количество побед', wins_counter1)
    print('Сумма очков', sum_of_points1)
elif wins_counter2 > wins_counter1:
    print('')
    print('Победил', igrok2)
    print('Количество побед', wins_counter2)
    print('Сумма очков', sum_of_points2)
else:
    print('')
    print('Ничья')


