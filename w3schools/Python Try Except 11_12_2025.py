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

# import sys
#
# def perform_risky_operation():
#
#     print("Виконую ризиковану операцію...")
#
#     try:
#         # Імітуємо неочікувану помилку, наприклад, ділення рядка на число
#         # або примусово викликаємо NameError
#         a = 10
#         if a > 5:
#     # Примусово викликаємо виняток, щоб протестувати обробник
#             raise NameError("Внутрішня помилка: Некоректна ініціалізація змінної.")
#
#     except Exception as err:
# # Перехоплюємо будь-який виняток і отримуємо його аргументи (повідомлення)
#         print("Виник неочікуваний виняток!")
#         print(f"Тип помилки: {type(err).__name__}")
# # Виведення повідомлення про помилку, що зберігається в об'єкті err
#         print(f"Деталі: {err}")
#
# perform_risky_operation()

'''Task 6: Handling errors when working with dictionaries (KeyError)'''
'''Задача 6: Обробка помилок при роботі зі словниками (KeyError)'''

# def safe_lookup(data: dict, key: str, default_value="The key is missing."):
"""Безпечно отримує значення зі словника або повертає значення за замовчуванням."""
#     try:
#         # спроба отримати значення за ключем
#         return data[key]
#     except KeyError:
#
#         return default_value
#
# #  dano
# user_profile = {'name': 'Oleg', 'city': 'Kyiv'}
#
# # test 1
# print(f"Ім'я: {safe_lookup(user_profile, 'name')}")
#
# # Test 2
# print(f"Вік: {safe_lookup(user_profile, 'age', 'Дані про вік відсутні')}")

'''Task 7: Handling errors in a try-except loop'''
'''Задача 7: Обробка помилок у циклі з try-except'''
#
# import math
#
# # list
# data_points = [4, 9, 16, -1, 'hello', 25, 0]
#
# print("Обчислення квадратного кореня:")
#
# for item in data_points:
#     try:
#         # спороба конвертувати в число
#         # Attempt to convert to a number and calculate the root
#         result = math.sqrt(float(item))
#         print(f"Root from {item} = {result}")
#
#     except (ValueError, TypeError) as e:
#         # Ігнорування недійсних даних та продовження циклу
#         print(f"Error in {item}: {type(e).__name__}. Пропуск.")
#         continue
#
# print("The list has been processed.")


'''Task 8: Using finally to clean up resources'''
'''Задача 8: Використання finally для очищення ресурсів'''
#
# def process_file_safely(filename, content, force_error=False):
# # """Відкриває та записує у файл, гарантуючи його закриття."""
#     file = None
#     try:
#         file = open(filename, 'w')
#         file.write(content + "\n")
#
#         if force_error:
#
#  # Спровокувати помилку для тестування блоку finally
#             1 / 0
#
#         print(f"Дані успішно записано у {filename}")
#
#     except ZeroDivisionError:
#         print("Помилка спроба ділення на нуль в блоці try.")
#
#     finally:
#         if file:
#             file.close()
#             print(f"Файл {filename} гарантовано закритою")
# # блок виконується завжди не залежно від помилки
#
# # test 1
# process_file_safely("log_safe.txt", "Getting started")
#
# # test 2
# process_file_safely("log_error.txt", "Data with error", force_error=True)


'''Task 9: Handling multiple exceptions simultaneously'''
'''Задача 9: Обробка кількох винятків одночасно'''
# Замість використання окремих блоків except для кожного типу помилок або
# використання загального except, що порушує чистоту коду,
# ми можемо перехопити кілька специфічних винятків одночасно

def calculate_average_safe(data):
    """Обчислює середнє значення, обробляючи TypeError та ZeroDivisionError."""
    try:
        result = sum(data) / len(data)
        print(f"Average value: {result}")

    except (TypeError, ZeroDivisionError) as e:
# Перехоплення кількох типів помилок однією гілкою
        if isinstance(e, ZeroDivisionError):
            print("Error: The list cannot be empty.")

        else:
            print(f"Error: Elements must be numbers. Exception: {type(e).__name__}")

# test 1
calculate_average_safe([])

calculate_average_safe([1, 2, 'a', 4])

calculate_average_safe([24-26])
