

data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designation = []
codes = []

for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designation.append(i)

print("Designation:", designation)
print("Codes:", codes)

operators = dict(zip(designation, codes))
print("Операторы:", operators)

operators.pop("Katel")
operators.pop("Fonex")
print("Операторы после удаление:", operators)

operators = {k: {v} for k, v in operators.items()}

operators["O!"].update(["0707", "0710"])
operators["Megacom"].update(["0555", "0999"])
operators["Beeline"].update(["0777", "0888"])

print("Итог:")
print(operators)

