
"""
def calculate_discount(hw_points, test_points, attendance):

    if 70 <= hw_points <= 80 and test_points > 80:
        return 3000
    elif 70 <= hw_points <= 80 and test_points > 60 and attendance >= 8:
        return 2500
    elif (70 <= hw_points <= 80 and test_points > 60) or \
         (60 <= hw_points <= 70 and test_points > 80) or \
        (50 <= hw_points <= 60 and test_points > 60 and attendance > 6):
        return 2000
    elif 50 <= hw_points <= 60 and test_points > 60:
        return 1000
    else:
        return 0  
hw = int(input("Баллы за ДЗ: "))
test = int(input("Баллы за тест: "))
att = int(input("Количество посещений: "))

discount = calculate_discount(hw, test, att)
print("Сумма скидки:", discount)

"""

# Словарь для конвертации кириллицы в латиницу
ru_to_en = {
    'й':'q','ц':'w','у':'e','к':'r','е':'t','н':'y','г':'u','ш':'i','щ':'o','з':'p',
    'х':'[','ъ':']','ф':'a','ы':'s','в':'d','а':'f','п':'g','р':'h','о':'j','л':'k',
    'д':'l','ж':';','э':'\'','я':'z','ч':'x','с':'c','м':'v','и':'b','т':'n','ь':'m',
    'б':',','ю':'.'
}

# Обратный словарь для латиницы в кириллицу
en_to_ru = {v: k for k, v in ru_to_en.items()}

def convert(text):
    text = text.lower()
    result = ''
    for ch in text:
        if ch in ru_to_en:
            result += ru_to_en[ch]
        elif ch in en_to_ru:
            result += en_to_ru[ch]
        else:
            result += ch
    return result

while True:
    word = input("Введите слово (для выхода введите 'q'): ")
    if word.lower() == 'q':
        break
    converted = convert(word)
    print("Результат:", converted)
