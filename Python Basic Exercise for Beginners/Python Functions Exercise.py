#'''Exercise 1: Create a function in Python'''
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


#'''Exercise 2: Create a function with variable length of arguments'''
# def func1(*args):
#     for value in args:
#         print(value)
#
# func1(10, 20, 30, 40)
# func1("Hello", True, 99, 3.15)

"""Exercise 3: Return multiple values from a function"""

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


'''Exercise 4: Create a function with a default argument'''

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


'''Exercise 5: Create an inner function'''
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


'''Exercise 6: Create a recursive function'''
# def recursive_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + recursive_sum(n - 1)
#
# result = recursive_sum(10)
# print(recursive_sum(10))

#numb2
# def addition(num):
#     print("Calling addition(",num,")")#щоб бачити результат функціїї
#     if num:
#         return num + addition(num - 1)
#     else:
#         return 0
#
# print(addition(10))


'''Exercise 7: Assign a different name to function and call it through the new name'''
#
# def display_student(name, age):
#     print(name, age)
#
# show_student = display_student
#
# show_student("Emma", 26)


'''Exercise 8: Generate a Python list of all the even numbers between 4 to 30'''

# even_nubers = [num for num in range(1, 31) if num % 2 == 0]
# print(even_nubers)


'''Exercise 9: Find the largest item from list'''

# x = [4, 6, 8, 24, 12, 2]
# print(max (x))

#інший спосіб без (max)

# x = [4, 6, 8, 24, 12, 2]
# largest = x[0]
#
# for num in x:
#     if num > largest:
#         largest = num
#
# print(largest)


'''Exercise 10: Call Function using both positional and keyword arguments'''
#
# def descride_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}, named {pet_name}.")
#
# descride_pet("hamster", "Harry")
# descride_pet("dog", "Lucia")
#
# descride_pet("cat", "Whid")
# descride_pet("Buddy", "goldfish")

'''Exercise 11: Create a function with keyword arguments'''
#
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#     else:
#         print("\nNone information provided")
#
# print_info(name="John", age=22, contry="USA")
# print("\n---\n")
# print_info(name="Andre", age=29, contry="123")

'''Exercise 12: Modifies global variable'''

# global_var = 10
#
# def modify_global():
#     global global_var #вказуємо що працюємо з глобальною змінною і потім змінюю
#     global_var = 20
#
# print("Before:", global_var)
# modify_global()
# print("After:", global_var)

'''Exercise 13: Write a recursive function to calculate the factorial'''

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# number = 5
# result = factorial(number)
# print(f"The factorial of {number} is {result}")

'''Exercise 14: Create a lambda function that squares a given number'''

# square = lambda x: x ** 2 #lambda arguments: expression'''
# #
# # print(square(4)) #
''' використання в циклі'''
# for i in range(10):
#     print(f"{i}^2 =", square(i))

'''Exercise 15: Use a lambda with the filter() function to get all even numbers from a list'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# event_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #бере лише ті елементи, які проходять умову
#
# print(f"Even numbers: {event_numbers}")

'''Exercise 16: Use a lambda with the map() function to double each element in a list'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# doubled_numbers = list(map(lambda x: x * 2, numbers)) #застосовує функцію до кожного елемента списку
#
# print(f"The doubled numbers are: {doubled_numbers}")

'''Exercise 17: Use a lambda with the sorted() function to sort a list of tuples based on the second element'''

# data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
# #сортування по другому елементу так як 0 рахується
#
# sorted_data = sorted(data, key=lambda item : item[1])
# print("The sorted list of tuples on the second elements is:", sorted_data)

#Є два списки фруктів: Перший містить фрукти, які є у магазині Другий — фрукти, які хоче купити покупець
# store = ['apple', 'banana', 'cherry', 'date', 'grape', 'kiwi']
# customer = ['kiwi', 'orange', 'banana', 'apple']

# available = list(filter(lambda fruit: fruit in store, customer))
#
# available_sorted = sorted(available, key=lambda x: x)
#
# print("Available fruits for customer: ", available_sorted)


# #інший варіант вирішення
# print("Available fruits for customer: ", sorted([fruit for fruit in customer if fruit in store]))

'''Exercise 18: Create Higher-Order Function'''

def apply_operation(func, x, y):
    return func(x, y)
"""
Applies a given function to two numbers.

  Args:
    func: The function to apply (should take two arguments).
    x: The first number.
    y: The second number.

  Returns:
    The result of calling func(x, y).
"""


def add(a, b):
    return a + b
resuld_add = apply_operation(add, 5, 3)
print(f"Result of addition: {resuld_add}")

subtract = lambda a, b: a - b
result_subtract = apply_operation(subtract, 10, 4)
print(f"Result of addition: {result_subtract}")

multipiy = lambda a, b: a * b
result_multiply = apply_operation(multipiy, 2, 6)
print(f"Result of multiplication: {result_multiply}")