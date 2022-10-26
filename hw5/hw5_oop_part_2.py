import dataclasses
from collections import namedtuple


#1.
class Laptop:
    """
    Make the class with composition.
    """
    def __init__(self, name):
        self.name = name
        battery = Battery('Lithium-ion')
        self.laptop = [self.name, battery.battery_type]


class Battery:
    """
    Make the class with composition.
    """
    def __init__(self, battery_type):
        self.battery_type = battery_type


dell = Laptop('Dell')
print(dell.laptop)

#2.
class Guitar:
    """
    Make the class with aggregation
    """
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    """
    Make the class with aggregation
    """
    def __init__(self, string_brand):
        self.string_brand = string_brand


d_addario_string = GuitarString("D'Addario")
fender_guitar = Guitar(d_addario_string)

#3
class Calc:
    """
    Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add_nums(self):
        return self.a + self.b + self.c


test = Calc(1,2,5)
print(test.add_nums())

#4*.
class Pasta:
    """
    Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
    Він повинен мати 2 методи:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients)
pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)


#5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """

    max_visitor_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= Concert.max_visitor_num:
            self._visitors_count = value
        else:
            self._visitors_count = Concert.max_visitor_num


Concert.max_visitor_num = 50
concert_test = Concert()
concert_test.visitors_count = 256
print(concert_test.visitors_count)

#6.
@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

#7. Create the same class (6) but using NamedTuple
AddressBook = namedtuple('AddressBook', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

#8.
class AddressBook2:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
    """
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __repr__(self):
        address_book_2_dict = dict(key=self.key, name=self.name, phone_number=self.phone_number,
                                   address=self.address, email=self.email, birthday=self.birthday,
                                   age=self.age)
        return f'AddressBook{(str(address_book_2_dict).replace("{","(").replace("}", ")"))}'

test_address_book = AddressBook2(2212, 'Olena', '09555555555', 'Lviv', 'olena_h@gmail.com', '1994', 28)
print(test_address_book.__repr__())

#9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    _age = 36
    country = "USA"

    def get_age(self):
        print("getter method called")
        return self._age

    def set_age(self, new_age):
        print("setter method called")
        self._age = new_age


galia = Person()
galia.set_age(18)
print(galia.get_age())

#10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.student_email = email


test_student = Student(23, 'Olena', 'olenah@gmail.com')
print(getattr(test_student, 'student_email'))