
#Списки, кортежы. Индексы и срезы. Встроенные функии к наборам элементов
#Списковые включение List comprehension

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))
print("geeks"[0])
print(numbers[0])
print(numbers[2])
print(numbers[-1])

#Срезы [start:stop:step]
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4:1])
print(numbers[1:4])
print(numbers[::])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::-2])
print("geesk"[::-1])

print(numbers[:2])
print(numbers[-2:])

#add
numbers = [1, 2, 3, 4, 5]
numbers.append(6) #добовляет только один элемент в конец
numbers.insert(3,9) #добовляет один элемент в нужный индекс
numbers.extend([6, 7, 8,"python"]) # numbers += [8, 9, 0] добовляет в конец несколько элементов

#edit
numbers = [1, 2, 3, 4, 5]
numbers[2] = 9
numbers[1] = 8
numbers[-2:] = [1,2]
numbers.reverse() #переворачивает список
print(numbers)
numbers.sort() #сортирует список

print(numbers)

#delete
numbers = [1, 2, 3, 4, 5, 2]
numbers.pop(0) #удаляет элемент в индексе
print(numbers)
numbers.remove(2)  #удаляет сам элемент (только один)
print(numbers)
del numbers[:2]  #удаляет несколько элементов 
print(numbers)
numbers.clear()  #очищает 
print(numbers)

#встроенные функции к наборам элементов.
cities = ["tokmok", "karakol", "bishkek", "kemin"]
print(cities)
cities_edited = [city.title() for city in cities if 'o' in city]
print(cities_edited)

#кортежы(turple) константа списков, нельзя менять значение
numbers = 1, 2, 3, 4, 5
numbers = (1, 2, 3, 4, 5)
print(numbers)
print(numbers[1])
print(type(numbers))
print(numbers.count(2))
print(numbers.index(2))
# кортеж содержать более 1 элемента, если только 1 элемент то не считается это кортежом
