
#Операторы: принадлежности, назначение. Циклы

#оператор принадлежности
print('p' in  'python')
print('pyth' in  'python')
print(5 in range(1,6))
print(5 in range(1,5))

#операторы назначение
# c+=a   c = c + a
# c-=a   c = c - a
# c*=a   c = c * a
# c/=a   c = c / a
# c%=a   c = c % a
# c**=a  c = c ** a
# c//=a  c = c // a

number = 5
print(number)
number += 3
number *= 4 
number -= 12
number **=2
print(number)


# while
counter = 0
while counter < 100:
    counter += 1
    if counter == 51:
        break
    #if counter == 42:
    #   continue

    if counter in range(22,25):
        print('...')
        continue
    print('hello', counter)


while True:
    time = input('времья сутки: ').lower()
    if time == 'stop':
        print('exit....')
        break
    
    if time == 'morning' or time == 'утро':
        print('good morning')
    elif time == 'day' or time == 'день':
        print('good afternoon')
    elif time == 'evening' or time == 'вечер':
        print('good everning')
    else: 
        print('hello (времья суток не определено)')

counter = 5
while counter > 0:
    time = input(f'времья сутки:({counter}) ').lower()
    
    if time == 'morning' or time == 'утро':
        print('good morning')
    elif time == 'day' or time == 'день':
        print('good afternoon')
    elif time == 'evening' or time == 'вечер':
        print('good everning')
    else: 
        print('hello (времья суток не определено)')
    counter -= 1



counter = 5
while counter > 0:
    day = int(input(f"{counter})Введите день вашего рождения: "))
    month = int(input("Введите месяц вашего рождения (числом): "))

    if (21 <= day <= 31 and month == 3) or (1 <= day <= 20 and month == 4):
        print("Овен")
    elif (21 <= day <= 30 and month == 4) or (1 <= day <= 21 and month == 5):
        print("Телец")
    elif (22 <= day <= 31 and month == 5) or (1 <= day <= 21 and month == 6):
        print("Близнецы")
    elif (22 <= day <= 30 and month == 6) or (1 <= day <= 22 and month == 7):
        print("Рак")
    elif (23 <= day <= 31 and month == 7) or (1 <= day <= 21 and month == 8):
        print("Лев")
    elif (22 <= day <= 31 and month == 8) or (1 <= day <= 23 and month == 9):
        print("Дева")
    elif (24 <= day <= 30 and month == 9) or (1 <= day <= 23 and month == 10):
        print("Весы")
    elif (24 <= day <= 31 and month == 10) or (1 <= day <= 22 and month == 11):
        print("Скорпион")
    elif (23 <= day <= 30 and month == 11) or (1 <= day <= 22 and month == 12):
        print("Стрелец")
    elif (23 <= day <= 31 and month == 12) or (1 <= day <= 20 and month == 1):
        print("Козерог")
    elif (21 <= day <= 31 and month == 1) or (1 <= day <= 19 and month == 2):
        print("Водолей")
    elif (20 <= day <= 29 and month == 2) or (1 <= day <= 20 and month == 3):
        print("Рыбы")
    else:
        print("Неверная дата! Попробуйте снова.")
    counter -= 1


saved_passvord = '12345'
counter = 5
while True:
    print(f'Осталось попыток: {counter}')
    input_passvord = input('enter passvord: ')
    if input_passvord == saved_passvord:
        print('пароль верный!')
        break
    if counter == 1:
        print('попыток не осталось!')
        break
    counter -= 1
 


for number in range(1,11):
    if number == 8:
        break
    if number % 2 != 0:
        continue
    print(number)





