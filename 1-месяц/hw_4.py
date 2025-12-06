


data_turple = ("h", 6.13, "C", "e", "T", True, "k", "e", 3, "e", 1, "g")
print(data_turple)
letters = []
numbers = []

# Разделяем буквы и числа
for item in data_turple:
    if type(item) == str:  # Проверяем, если элемент - строка
        letters.append(item)
    else:
         numbers.append(item) #а остаальное в numbers

print("Буквы:", letters)
print("Числа:", numbers)

numbers.remove(6.13) #del 6.13
numbers.remove(True) #del True
print("Числа:", numbers) 
letters.append(True)  #add True в конец списка
print("Буквы:", letters)

numbers.insert(1,2)   #add 2 между 3 и 1
print("Числа:", numbers) 
numbers.sort()        # sort 
print("Числа:", numbers) 

letters.reverse()   #реверсировать
print("Буквы:", letters)
letters[1] = "G"
letters[7] = "c"
print("Буквы:", letters)

numbers = [x**2 for x in numbers]  #квадраты своих же чисел
print("Числа:", numbers) 

numbers_tuple = tuple(numbers)   #преоброзовать списки в кортежи
letters_tuple = tuple(letters)
print("Числа как кортеж:", numbers_tuple)
print("Буквы как кортеж:", letters_tuple)