
#Логический тип данных
print(10 == 2)
print(10 > 2)
print(10 <= 2)

#Операторы сравнение
print('abs123' =='abs124')
print('abs123' =='abs123')

#Логические операторы
print(2 > 1 and 1 < 4)
print(2 > 1 and 1 < 0)
print(2 > 1 or 1 < 0)
print(not False)
print(not True)


time = input('времья сутки: ').lower()

if time == 'morning' or time == 'утро':
    print('good morning')
elif time == 'day' or time == 'день':
    print('good afternoon')
elif time == 'evening' or time == 'вечер':
    print('good everning')
else: 
    print('hello (времья суток не определено)')


#холодно = от -40 до 5
#прохладно = от 6 до 15
#тепло = от 16 до 25
#жарко = от 26 до 40
#не выходи на улицу

temperature = int(input('введите температуру: '))
if temperature >= -40 and temperature <=5:
    print('холодно')
elif temperature >= 6 and temperature <=15:
    print('прохладно')
elif temperature >= 16 and temperature <=25:
    print('тепло')
elif temperature >= 26 and temperature <=40:
    print('жарко')
else:
    print('не выходи на улицу')

