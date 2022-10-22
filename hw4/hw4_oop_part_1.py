#1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed, mileage_info
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self, increase):
        print(f'Speed has been increased by {increase} mph')

    def break_speed(self, reduced_speed):
        print(f'Speed has been reduced by {reduced_speed} mph')

    def mileage_info(self):
        print(f"Mileage info: {self.mileage}")

daewoo_lanos = Vehicle(100, 12345)
daewoo_lanos.increase_speed(5)
daewoo_lanos.break_speed(2)
daewoo_lanos.mileage_info()

#2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод seating_capacity
class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self, capacity):
        print(f"The seating capacity of the bus is {capacity} passengers")

sprinter = Bus(80, 12000)
sprinter.seating_capacity(100)

#3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
print(f'Bus class is a subclass of Vehicle class? {issubclass(Bus, Vehicle)}')

#4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus
school_bus = Bus(50, 12000)
print(f'School bus is an instance of Bus class? {isinstance(school_bus, Bus)}')
print(f'School bus is an instance of Vehicle class? {isinstance(school_bus, Bus)}')

#5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address, main_subject
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_address(self, school_address):
        print(f'The school address is {school_address}')

    def main_subject(self, main_subject):
        print(f'The main subject of this school is {main_subject}')

school_10 = School(123, 5000)
school_10.school_address('Lviv, Chuprynky 1')
school_10.main_subject('maths')

#6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color
class SchoolBus(School, Bus):
    def bus_school_color(self, bus_school_color):
        print(f'The bus school color is {bus_school_color}')

school_bus_10 = SchoolBus((50, 12000),(123, 5000))
school_bus_10.bus_school_color('green')

#7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,
class Bear:
    def eat(self):
        print("Bear is eating")

class Wolf:
    def eat(self):
        print("Wolf is eating")

bear_1 = Bear()
wolf_1 = Wolf()

animals_tuple = (bear_1, wolf_1)

for animal in (bear_1, wolf_1):
    animal.eat()

#Додатково: 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу,
# лише коли population > 1500,
#інакше повертається повідомлення: "Your city is too small". Підказка: використовуєте для цього завдання магічні методи

class City:
    def __new__(cls, name, population):
        if population > 1500:
            return object.__new__(cls)
        else:
            print("Your city is too small")
    def __init__(self, name, population):
        self.name = name
        self.population = population
        print(f"Welcome to {self.name}")

lviv = City("Lviv", 721301)
vynnyky = City("Vynnyky", 1499)