#hw_1

def ifpassword(password):
    if len(password) < 6:
        return False

    has_digit = False
    has_upper = False
    has_lower = False
    special_count = 0

    specials = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"

    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch in specials:
            special_count += 1

    return has_digit and has_upper and has_lower and special_count >= 2


password = input("Введите пароль: ")

if ifpassword(password):
    print("Надежный пароль")
else:
    print("Ненадежный пароль")


#hw_2

def nearest_number(numbers, target):
    min_distance = 0
    nearest = None

    for num in numbers:
        dist = abs(num - target)
        if min_distance == 0 or dist < min_distance:
            min_distance = dist
            nearest = num

    return nearest


numbers = [1, 2, 5, 6, 9]
target = 8

result = nearest_number(numbers, target)

print("Список:", numbers)
print("Целевое число:", target)
print("Эң жакын сан:", result)
