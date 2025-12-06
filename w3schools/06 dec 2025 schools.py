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

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

print(my_dict)

# del profession
# del my_dict['profession']
my_dict.pop('profession')

print(f'del profession: {my_dict}')

# виведення усіх ключ значень output of all key values
for key, value in my_dict.items():
    print(f'{key}: {value}')

# True if age is in the list чи є значення в списку
is_age_present = 'age' in my_dict

print(is_age_present)

