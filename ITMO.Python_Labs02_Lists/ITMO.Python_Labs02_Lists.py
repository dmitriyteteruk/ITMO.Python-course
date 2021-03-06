print("##### Работа со списками #####")
print('')
list1 = [82, 8, 23, 97, 92, 44, 17, 39,11, 12]
print(list1)
print('')
# insert, append, sort, remove, reverse

# Измените значения элементов списка (по вашему усмотрению) с помощью операции индексирования.
list1[2] = 1000
print(list1)
print('')

# Добавьте новый элемент в конец списка
list1.append(999)
print(list1)
print('')

# Добавьте новый элемент в произвольную (на ваше усмотрение) позицию списка
list1.insert(0, 777)   # 0 - номер индекса для добавляемго значения, 777 - само значение
print(list1)
print('')

# Удалите элемент из списка по известной позиции
list1.pop(0)
print(list1)
print('')

# Удалите последний элемент из списка
list1.pop(len(list1)-1)
print(list1)
print('')

print("##### Сортировка #####")
print(list1, " - лист без сортировки")
list1.sort(reverse=True)     # sort меняет местами значения в исходном списке
print(list1, " - отсортированный лист (reverse=True)")
print('')
list_sorted = sorted(list1)     # sorted не меняет исходный список, а создает новый
print(list_sorted, " - новый отсортированный лист через sorted")      
print(list1, " - лист без сортировки")
print('')

print("##### Работа с кортежами #####")
print('')

# Определите, что возвращают команды
seq = (2,8,23,97,92,44,17,39,11,12,8)
print(seq, " - кортеж")
print(seq.count(8), " :count(8) - возвращает кол-во элементов с заданным значением")
print(seq.index(44), " :index(44) - возвращает номер индекса первого элемента совпавшего со значением") 
print('')

# Преобразуйте кортеж к типу «список»
print(type(seq), " - класс (тип) кортеж (tuple)")
listseq = list(seq)
print(type(listseq), " - класс (тип) после преобразования  список (list)")
print('')

# Проверьте работу основных методов, применяемых к списку для преобразованного «кортежа».
listseq.sort(reverse=True)
print(listseq, "сортировка reverse=True")
listseq.append(999)
print(listseq, "append(999)")
del listseq[-1]
print(listseq, "del list[-1] ")
listseq.pop(len(listseq)-1)
print(listseq, "pop(len(list) -1 ")
print('')

print("##### Работа со словарями #####")
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
D['quantity'] += 10
print(D)
print('')

# Напишите инструкцию, заполняющую словарь значениями, 
# вводимыми с клавиатуры в создаваемые ‘на лету’ ключи ‘name’ и ‘age’.


dp = {}
print(dp, " - пустой словарь")
name = str(input("Введите имя: "))
age = int(input("Введите возраст: "))
dp[name] = age
name = str(input("Введите имя: "))
age = int(input("Введите возраст: "))
dp[name] = age
name = str(input("Введите имя: "))
age = int(input("Введите возраст: "))
dp[name] = age
print(dp, " - заполненный словарь")
print('')

# Требуется реализовать сложную структуру представления данных о некой персоне, 
# включающая имя и фамилию, несколько названий должностей, занимаемых одновременно, а также возраст.
# Реализуйте вывод значения полного имени, отдельно имени firstname, список должностей

rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
        'job': ['dev', 'mgr'],
        'age': 25}
print(rec['name']['firstname'], rec['name']['lastname'], " - полное имя")
print(rec['name']['firstname'], " - отдельно firstname")
print(rec['job'], " - список должностей")