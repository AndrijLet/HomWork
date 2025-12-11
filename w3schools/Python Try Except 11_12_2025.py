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
def get_valid_age():

    while True:
        try:
            age_inpyt = input("Please enter your age (integer): ")
            age = int(age_inpyt)
            print(f"You are {age} years old")
            break # Вихід з циклу, якщо введення успішне

        except ValueError:
            print("Incorrect input. Please enter an integer.")

get_valid_age()
