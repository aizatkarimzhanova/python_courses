#Базовый синтаксис, переменные, комментарии, встроенные функции.
#Типы данных(базовые):строки, целые и дробные числа. Арифметические операторы
print('hello world')

name = 'aizat'
surname = 'karimzhanova'
age = 19
height = 1.76

print(type(age))
print(type(height))

print(name, surname)
print(name.title(), surname.upper())
print(f'1)fullname: {name} {surname}')

"""Арифметические операторы"""
print(5 ** 3) #степень
print(7 // 2) #деление в котором возвращается только целая часть результата
name = input('what is your name? ').title()
surname = input('what is your surame? ').title()
age = int(input(f'{name}, please enter your age: '))
current_year = 2025
born = current_year - age

print(f"fullname: {name} {surname} born:{born}")