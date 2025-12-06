
#Словари-dict и множества
#{key:value}
student = {
    "name":"Aizat",
    "age": 18 ,
    "married": False
}
print(student)
print(student["name"])
print(student["age"])
print(student["married"])
print(type(student))

#add
student["weight"] = 52.2
student.update({"country":"KGZ", "heignt":1.65}) 

#edit
student["name"] = "Aiz"

#delete
student.pop("age")
del student["country"]
print(student)

countries_list = ["KGZ", "KAZ", "UZB", "RUS"] #список
countries_dict = {"KGZ":"Bishkek",
                  "KAZ":"Astana",
                  "UZB": "tashkent"
                  }                           #словарь
print(countries_list)
print(countries_dict)

#for i in countries_dict:
#    print(f"{i}: {countries_dict[i]}")
print(countries_dict.keys())
print(countries_dict.values())
print(countries_dict.items())

for key, value in countries_dict.items():
    print(f"{key}: {value}")

countries_dict = {"KGZ":"Bishkek",
                  "KAZ":"Astana",
                  "UZB": "tashkent"
                  }

print(countries_dict)

#если в гет есть такой ключ то берет его значение 
#а если нет выведет на экран следующее слово
print(countries_dict.get("KAZ","нет такого ключа"))
print(countries_dict.get("rus","нет такого ключа"))


numbers1 = [1, 2, 3, 4, 1, 3, 5] #список
numbers2 = (1, 2, 3, 4, 1, 3, 5) #кортеж
numbers3 = {1, 2, 3, 4, 1, 3, 5} #множество

print(numbers1)
print(numbers2)
print(numbers3)
print(type(numbers3))  #set


beshbarmak = {"мясо", "тесто", "лук"}
plow = {"рис", "морковь", "мясо"}
print(beshbarmak.union(plow))
print(beshbarmak.difference(plow))
print(beshbarmak.intersection(plow))
print(beshbarmak.symmetric_difference(plow))



