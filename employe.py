import string
import re
import faker

fake = faker.Faker("fr_FR")

class Employe:
    def __init__(self, first_name:str, last_name:str, phone_number:str):
        self.id = Employe.generate_id()
        self.first_name = Employe.check_name(first_name)
        self.last_name = Employe.check_name(last_name)
        self.phone_number = Employe.check_phone_number(phone_number)
        self.is_active = True

    def update_info(self, data:dict):
        print(type(self), self)


    @classmethod 
    def generate_id(cls):
        return 'SN' + str(fake.unique.random_number(digits=4))

    @classmethod
    def check_name(cls, name):
        special_characters = string.punctuation + string.digits
        for char in name:
            if char in special_characters:
                raise ValueError("Invalid name")
        return name

    @classmethod
    def check_phone_number(cls, phone_number):
        correct_phone_number = re.sub(r'\D', "", phone_number)
        if len(correct_phone_number) < 10 or not correct_phone_number.isdigit():
            raise ValueError("Invalide phone number")
        return phone_number