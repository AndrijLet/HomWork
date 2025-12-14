'''Write a program that asks the user for two numbers and performs division.'''
#Обробка помилки ділення на нуль (ZeroDivisionError)
# def safe_divide():
#     try:
#         numerator = float(input("Enter the numerator: "))
#         denominator = float(input("Enter the denominator: "))
#
#         result = numerator/denominator
#         print(f"Result: {result}")
#
#     except ZeroDivisionError:
#         print("Error: Division by zero is not possible. Try another number.")
#     except ValueError:
#         print("Error: An incorrect numerical value has been entered.")
# # додатково якщо ввели не число
# safe_divide()

'''Write a program that asks the user to enter an integer.'''
#Напишіть програму, яка просить користувача ввести ціле число (наприклад, вік),
# але має бути стійкою до ситуації, коли користувач вводить текст або дробове число.
# def get_valid_age():
#
#     while True:
#         try:
#             age_inpyt = input("Please enter your age (integer): ")
#             age = int(age_inpyt)
#             print(f"You are {age} years old")
#             break # Вихід з циклу, якщо введення успішне
#
#         except ValueError:
#             print("Incorrect input. Please enter an integer.")
#
# get_valid_age()

''' Intercept ValueError and ask the user to repeat the input or display an informative message.'''
#  Перехопіть ValueError і попросіть користувача повторити введення або виведіть інформативне повідомлення
#
# def get_valid_age():
# # Запитує вік, доки не отримає коректне ціле число
#     while True:
#         try:
#             age_input = input("Enter your age (integer): ")
#             age = int(age_input)
#             print(f'You are {age} years old.')
#             break #Вихід з циклу, якщо введення успішне
#         except ValueError:
#             print("Incorrect input. Please enter an integer.")
#
# get_valid_age()

'''Checking for file existence (FileNotFoundError)'''
# Перевірка наявності файлу (FileNotFoundError)

# def read_user_file():
#
#
#     """Спроба відкрити файл, вказаний користувачем, з обробкою FileNotFoundError."""
# file_name = input("Please enter the file name: ")
#
# try:
#     with open(file_name, 'r', encoding='utf-8') as file:
#         content = file.read()
#     print("\nВміст файлу:")
#     print(content)
# except FileNotFoundError:
#     print(f"Error: File '{file_name}' not found.")
#
# read_user_file()

'''Task 4: Handling errors in nested structures (KeyError and IndexError)'''
'''Задача 4: Обробка помилок у вкладених структурах (KeyError та IndexError)'''
# Приклади
# Ситуація	                    Виняток
# Файлу не існує	            FileNotFoundError
# Ділення на нуль	            ZeroDivisionError
# Неправильне ім’я змінної	    NameError
# Не той тип даних	            TypeError
# # Неправильний індекс	        IndexError
#
# user_data = {
#     'tasks': ['купити хліб', 'відповісти на листа', 'програмування'],
#     'status': 'active'
# }
#
# def get_task_by_index(data, key, index):
#     """Отримує елемент зі списку в словнику, обробляючи KeyError та IndexError."""
#     try:
#         task_list = data[key]
#         task = task_list[index]
#         print(f"Завдання знайдено: {task}")
#
#     except KeyError:
#         print(f"Помилка: Ключ '{key}' не знайдено у словнику.")
#
#     except IndexError:
#         print(f"Помилка: Індекс {index} виходить за межі списку завдань.")
# print("\n--- Спроба 3 (IndexError) ---")
# get_task_by_index(user_data, 'tasks', 0)


# print("\n--- Спроба 2 (KeyError) ---")
# get_task_by_index(user_data, 'projects', 0)

# print("--- Спроба 1 (Успіх) ---")
# get_task_by_index(user_data, 'tasks', 1)


'''Task 5: Using a generic handler and accessing exception arguments (Exception as err)'''
'''Задача 5: Використання загального обробника та доступу до аргументів винятку (Exception as err)'''

import sys

def perform_risky_operation():

    print("Виконую ризиковану операцію...")

    try:
        # Імітуємо неочікувану помилку, наприклад, ділення рядка на число
        # або примусово викликаємо NameError
        a = 10
        if a > 5:
    # Примусово викликаємо виняток, щоб протестувати обробник
            raise NameError("Внутрішня помилка: Некоректна ініціалізація змінної.")

    except Exception as err:
# Перехоплюємо будь-який виняток і отримуємо його аргументи (повідомлення)
        print("Виник неочікуваний виняток!")
        print(f"Тип помилки: {type(err).__name__}")
# Виведення повідомлення про помилку, що зберігається в об'єкті err
        print(f"Деталі: {err}")

perform_risky_operation()