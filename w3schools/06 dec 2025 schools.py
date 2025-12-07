
# my_dict = {
#     'name': 'Alice',
#     'age': 35,
#     'city': 'New York'
# }
#
# print(my_dict)
#
# my_dict['profession'] = 'Doctor'
# print(my_dict)
#
# my_dict['age'] = 40
#
# print(my_dict)
# # print("City:", my_dict['city'])
# print(f'City: {my_dict["city"]}')

'''Exercise 2: Perform dictionary operations'''

# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
#
# print(my_dict)
#
# # del profession
# # del my_dict['profession']
# my_dict.pop('profession')
#
# print(f'del profession: {my_dict}')
#
# # виведення усіх ключ значень output of all key values
# for key, value in my_dict.items():
#     print(f'{key}: {value}')
#
# # True if age is in the list чи є значення в списку
# is_age_present = 'age' in my_dict
#
# print(is_age_present)

'''Exercise 3: Dictionary from Lists'''
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

#основний спосіб zip для об'єднання списків у пари (ключ, значення)
# і dict() для перетворення цих пар на словник

# res_dict = dict(zip(keys, values))
# print(res_dict)

# Використовуємо zip() для створення пар, а потім словникове включення
# для визначення формату ключ:значення

# result_dict_comp = {key: value for key, value in zip(keys, values)}
# print(result_dict_comp)

#менш лаконічним, але демонструє покрокову логіку
# result_dict_loop = {}
# # Ітерація по парах (ключ, значення), створених за допомогою zip()
#
# for key, value in zip(keys, values):
#     result_dict_loop[key] = value
#     print(result_dict_loop)

'''Exercise 4: Clear Dictionary'''

# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

# print(f'my_dict: {my_dict}')
#
# my_dict.clear()
# print(f'dictionary after: {my_dict}')

'''Exercise 5: Merge two Python dictionaries into one'''
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# print(f'{dict1}\n{dict2}')
# #для об'єднання словників у Python, який застосовує оператор розпакування (**)
# dict3 = {**dict1, **dict2}
# print(f'{dict3}')

'''Exercise 6: Count Character Frequencies'''

from collections import Counter
string1 = 'Jessa'

# Використовуємо Counter для автоматичного підрахунку частот символів
char_frequency = Counter(string1)

print(f"Frequency of '{string1}' : {dict(char_frequency)}")

