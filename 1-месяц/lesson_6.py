
# Функции: виды параметров,возвращение данных, виды аргументов

#определение наименование(параметры):
#    тело функции(вычисление, логика)
#    возвращение объекта

#вызов функции
#наименование (аргменты)

def func_name(name, surname ="unknown"): #required positional parameter (объезательные позиционные параметры)
    print(f"name:{name} surname:{surname}")

func_name("Aizat", "Karimzhanova")  #required positional argument (объезательный позиционный аргумент)
func_name(surname="Kasymbekova", name="Aliya") #keywords arguments (ключевые аргументы)
func_name("Roza")

def get_square(length, width):
    square = length * width
    return f"lendth({length}) * width({width}) = square({square})"

square_2 = get_square(7, 5)
square_coworking = get_square(20, 10)
print(square_2)
print(square_coworking)

def get_square(length: int, width: int) -> str:
    """тут нужно брать только целые(int) значение (length, width)
     значение возвращается в типе str """
    square = length * width
    return f"lendth({length}) * width({width}) = square({square})"

numbers = [23, 32, 47, 48]
amount_objects = len(numbers)
print(amount_objects)
print(type(amount_objects))

def len1(iterable):
    counter = 0
    for _ in iterable:
        counter += 1
    return counter
amount_objects1 = len1(numbers)
print(amount_objects1)
print(type(amount_objects1))

def plus(numbers):
    amount = 0
    for num in numbers:
        amount += num
    return amount
numbers = [1, 2, 3, 5, 7 ]
print(plus(numbers))

print(plus([21, 33, 4]))

def plus(*args):    #кортеж
    return sum(args)
print(plus(21, 33, 4))


def menu(**kwargs):
    return kwargs
mon = menu(a=2, b=12, m=22)
print(mon)
