class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    def validate_phone_number(phone_number):
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        else:
            return False
print(Contact.validate_phone_number("1234567890"))


    


