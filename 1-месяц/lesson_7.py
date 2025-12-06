
# Lamda функции. Обработка исключений

def up_firsr_letter(word: str):
    return word.title()

def upper_1(word: str):
    return word.upper()

print(up_firsr_letter("aizat"))

def show_words(func, words):  #функиянын ичинде функция жургузууго болот.М:up_firsr_letter,upper_1
    for word in words:
        print(func(word))

word_list = ["pen", "red", "car", "ball", "blue", "yellow"]
show_words(up_firsr_letter, word_list)
show_words(len, word_list)


#
def def_f(n1, n2):
    return n1 + n2
print(def_f(2, 3))
#
lambda_f = lambda n1, n2: n1 + n2
print(lambda_f(2, 3))


def show_words(func, words):  
    for word in words:
        print(func(word))

#      
word_list = ["pen", "red", "car", "ball", "blue", "yellow"]
show_words(lambda word: word.title(), word_list) 
# sorted, filter, map 
word_list = ["pen", "red", "car", "ball", "blue", "yellow"]
print(word_list)

#sorted_words = sorted(word_list, key=lambda word: word[1])
#print(sorted_words)

#filter_words = list(filter(lambda word: len(word) > 3, word_list))
#print(filter_words)

#map_words = list(map(lambda word: word.upper() + "*", word_list))
#print(map_words)

#
try:
    print(2 + "dc")
except Exception as error:
    print(f"обнаружена ошибка! ({error})")
else:
    print("ошибка не обнаружена!")
finally:
    print("проверка завершена!")


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

 




