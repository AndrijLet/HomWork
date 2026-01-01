'''OOP Exercise 1: Create a Class with instance attributes'''
#
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_sped = max_speed
#         self.mileage = mileage
#
# modelX = Vehicle(240, 18)
# print(modelX.max_sped, modelX.mileage)

# Перевага: Такий підхід підвищує гнучкість класу, дозволяючи створювати об'єкти без аргументів, якщо це необхідно
# class Vehicle:
#     def __init__(self, max_sped=150, mileage=10):
#         self.max_sped = max_sped
#         self.mileage = mileage
# modelX_custom = Vehicle(240, 18
#                         )
# print(f"Custom Model: {modelX_custom.max_sped} / {modelX_custom.mileage}")

# class Vehicle:
#     def __init__(self, max_speed: int, mileage: int):
#         # Анотації тут лише інформують, але не встановлюють типи.
#         self.max_speed = max_speed
#         self.mileage = mileage

'''OOP Exercise 2: Create a Vehicle class without any variables and methods'''
# class Vehicle:
#     pass

'''OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class'''
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def __str__(self):
#         return f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"
# """Повертає атрибути об'єкта у потрібному форматі."""
# # Використання f-рядків забезпечує ясність і лаконічність
#
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 180, 12)
#
# print(School_bus)

'''OOP Exercise 4: Class Inheritance'''

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)
#
# School_bus = Bus("School Volvo", max_speed=180, mileage=12)
# print(School_bus.seating_capacity())

'''OOP Exercise 5: Define a property that must have the same value for every class instance (object)'''

# class Vehicle:
#     color = "White"
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
#
# car = Car("Audi Q5", 240, 18)
# print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)


'''OOP Exercise 6: Class Inheritance'''

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         base_fare = super().fare()
#         """Розрахунок вартості для автобуса з урахуванням 10% націнки."""
#         # Отримуємо базову вартість від батьківського класу через super()
#         total_fare = base_fare + (base_fare * 10 / 100)
# #         додаємо 10% до суми
#         return total_fare
#
# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())

'''OOP Exercise 7: Check type of an object'''

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 12, 50)
#
# print(type(School_bus))

# можна застосувати функцію isinstance(), яка перевіряє, чи є об'єкт
# екземпляром конкретного класу або будь-якого класу в його ієрархії успадкування
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 12, 50)

# print(f'Class: {type(School_bus)}')
# if isinstance(School_bus, Bus):
#     print("Bus Class Inheritance")

'''OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class'''

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 12, 50)
#
# print(isinstance(School_bus, Vehicle))

'''OOP Exercise 9: Check object is a subclass of a particular class'''

# class Animal:
#     pass
#
# class Dog(Animal):
#     pass
#
# class Puppy(Dog):
#     pass
#
# class Cat:
#     pass
#
# print(issubclass(Dog, Animal))
# print(issubclass(Animal, Dog))
# print(issubclass(Cat, Animal))
# print(issubclass(Puppy, Animal))

'''OOP Exercise 10: Calculate the area of different shapes using OOP'''

# import math
#
# class Shape:
#     def area(self):
#         raise NotImplementedError('Area method must be implemented by subclasses')
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
# # Example of polymorphism
# shapes = [Circle(5), Square(7), Circle(3)]
#
# for shape in shapes:
#     print(shape.area())  # Output: 78.53975, 49, 28.27431


'''OOP Exercise 10'''
#
# class Employee:
#     def calculate_salary(self):
#         raise NotImplementedError("This method must be implemented in subclasses")
#
# class HourlyEmployee(Employee):
#     def __init__(self, hours, rate):
#         self.hours = hours
#         self.rate = rate
#
#     def calculate_salary(self):
#         return self.hours * self.rate
#
# class SalariedEmployee(Employee):
#     def __init__(self, monthly_salary):
#         self.monthly_salary = monthly_salary
#
#     def calculate_salary(self):
#         return self.monthly_salary
#
# employees = [
#     HourlyEmployee(hours=160, rate=10),
#     SalariedEmployee(3000),
#     HourlyEmployee(hours=120, rate=15),
# ]
#
# for emp in employees:
#     print(emp.calculate_salary())


'''OOP Exercise 11'''
# class Employee:
#     def calculate_salary(self):
#         raise NotImplementedError("This method is not implemented in subclass")
#
# class CommissionEmployee(Employee):
#     def __init__(self, base_salary, sales, percent):
#         self.base_salary = base_salary
#         self.sales = sales
#         self.percent = percent
#
#     def calculate_salary(self):
#         return self.base_salary + (self.sales * self.percent / 100)
#
# class HourlyEmployee(Employee):
#
#     def __init__(self, hours, rate):
#         self.hours = hours
#         self.rate = rate
#
#
#     def calculate_salary(self):
#         return self.hours * self.rate
#
# employees = [
#     CommissionEmployee(2000, 5000, 10),
#     HourlyEmployee(160, 15)
# ]
#
# for employee in employees:
#     print(employee.calculate_salary())

'''OOP Exercise 12'''
# class Employee:
#     def calculate_salary(self):
#         raise NotImplementedError("Please implement calculate_salary")
#
# class HourlyEmployee(Employee):
#     def __init__(self, hours, rate):
#         self.hours = hours
#         self.rate = rate
#
#     def calculate_salary(self):
#         return self.hours * self.rate
#
# class SalaryEmployee(Employee):
#     def __init__(self, monthly_salary):
#         self.monthly_salary = monthly_salary
#
#     def calculate_salary(self):
#         return self.monthly_salary
#
# employees = [
#
#     HourlyEmployee(160, 15),
#     SalaryEmployee(3000)
# ]
#
# for employee in employees:
#     print("Salary:", employee.calculate_salary())

# print(isinstance(HourlyEmployee(10, 5), Employee))