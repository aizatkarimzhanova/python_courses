

#1
def nearest_numbers(numbers, target):
    sorted_by_distance = sorted(numbers, key=lambda x: abs(x - target))
    return target, sorted_by_distance


numbers = [996, 312, 31, 1991]
target = 1000

result = nearest_numbers(numbers, target)
print(result)


#2
# этот код возведет все числа списка в квадрат
nums = [1, 2, 3, 4]
result = list(map(lambda x: x**2, nums))
print(result)

#оставит только четных чисел
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)


#3
def get_element(iterable=None):
    if iterable is None:
        iterable = (1, 2, 5, 6, 9, 10, 15, 20)

    n = len(iterable)
    print("Iterable:", iterable)
    print(f"Допустимые индексы: 0 .. {n - 1}")
    print("Введите индекс или 'exit' для выхода.")

    while True:
        user_input = input("Индекс: ")

        if user_input.lower() == "exit":
            print("Выход.")
            break

        try:
            idx = int(user_input)
        except ValueError:
            print("Ошибка: нужно ввести число или 'exit'.")
        else:
            if 0 <= idx < n:
                print(f"Значение: {iterable[idx]}")
            else:
                print(f"Ошибка: допустимый диапазон индексов 0 .. {n - 1}")

get_element()


