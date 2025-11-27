#Exercise 1: Create a function in Python
# def demo(name, age, city):
#     print(name, age, city)
#
# demo("Bohdan", 22, "Ham")

#отримуємо дані користувача з допомогою функції та виводимо їх
# def demo(name, age, city):
#     print(name, age, city)
#
# user_name = input("Enter your name: ") #отримуємо дані користувача імя
#
# user_age = int(input("Enter your age: ")) #конвертуємо введений вік у число
# user_city = input("Enter your city: ") #отримуємо дані місця проживання
# demo(user_name, user_age, user_city) # передаємо дані у функцію для виведення


#Exercise 2: Create a function with variable length of arguments
# def func1(*args):
#     for value in args:
#         print(value)
#
# func1(10, 20, 30, 40)
# func1("Hello", True, 99, 3.15)

#Exercise 3: Return multiple values from a function

# def calculation(a, b):
#     addition = a + b
#     subtraction = a - b
#     return addition, subtraction #повернення обидва значення
# #виклик функції
#
# res = calculation(2, 3)
# print(res)

# def calculation(a, b):
#     return a + b, a - b
#
# add, sub = calculation(50, 40)
# print(add, sub)


#Exercise 4: Create a function with a default argument

# def show_employee(name, salary=9000):
#     print("Name:", name, "Salary:", salary)
#
# show_employee("Ben", 12000)
# show_employee("Kali")

# def rectangle_area(length,width):
#     area = length * width
#     return area
#
# l = float(input("Enter the length of the rectangle: "))
# w = float(input("Enter the width of the rectangle: "))
#
# result = rectangle_area(l,w)
#
# print(f"The area of the rectangle is {result}")
#
# def rectangle_area(length,width):
#     return round(length * width, 2)
#
# def rectangle_perimeter(length,width):
#     return round(2 * (length + width), 2)
#
# l = float(input("Enter the length of the rectangle: "))
# w = float(input("Enter the width of the rectangle: "))
#
# if l > 0 and w > 0:
#     area = rectangle_area(l,w)
#     perimeter = rectangle_perimeter(l,w)
#     print(f"The area of the rectangle is {area}")
#     print(f"The perimeter of the rectangle is {perimeter}")
#
# else:
#     print("Please enter a valid length and width")


#Exercise 5: Create an inner function
# def oter_fun(a, b):
#     square = a ** 2
#
#     #внутрішня функція
#     def addition(a, b):
#         return a + b
#     #виклик функції з параметром
#     add = addition(a, b)
#
#     #дадаємо 5 до результатів inner функції та повертаємо
#     return add + 5
# result = oter_fun(5, 10)
# print(result)




# def outer(a, b): #аргументи
#     print(f"outer() called with a={a}, b={b}")
# #оголошення inner - внутрішня функція
#     def inner():
#         print(" inner() called with a + b")
#         s = a + b
#         print(f" inner() computed s = {s}")
#         return s
#
#     sum_ad = inner()
#     print(f"outer() received sum_ad = {sum_ad} from inner()")
#
#     result = sum_ad + 5
#     print(f"outer() adds 5 -> result = {result}")
#
#     return result
#
# print("final returned valute:", outer(10, 20))
