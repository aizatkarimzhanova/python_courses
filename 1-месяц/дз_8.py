
keyword_list = """False            class          from         or    
None              contunue         global         pass
True              def              if             raise 
and               del              import         return
as                elif             in             try
assert            else             is             while
async             except           lambda         with
await             finally          nonlocal       yield
break             for              not """.split()
keyword_list_amount = len(keyword_list)
counter_1 = 0
data = {}
word_dict = {}

for keyword in keyword_list:
    answer = input(f"проходили/не проходили ({keyword})? ")
    if answer:
        data[keyword] = True
    else:
        data[keyword] = False

for key, value in data.items():
    print(f"{key}: {value}")
    word_dict[key] = value

for key, value in word_dict.items():
    if value == True:
        counter_1 += 1
print(word_dict)
print(f"Общая количество ключевых слов: {keyword_list_amount}")
print(f"Количество пройденных слов: {counter_1}")

prosent = int((counter_1 / keyword_list_amount) * 100)
print(f"{prosent}% пройдено из общего количества")
