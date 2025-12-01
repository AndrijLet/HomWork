# def filter_list(data, condition):
#     return [item for item in data if condition(item)]
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# is_even = lambda x: x % 2 == 0
# is_odd = lambda x: x % 2 != 0
#
# result = filter_list(list1, is_even) + filter_list(list2, is_odd)
# print("Third list: ", result)

"""GPT"""
# def filter_list(data, is_valid):
#      return [item for item in data if is_valid(item)]
#
# numbers = [3, 15, 8, 22, 7, 19]
#
# is_even = lambda x: x >10
#
# result = filter_list(numbers, is_even)
# print(result)

"""GPT2"""
# def filter_list(data, is_valid):
#      return [item for item in data if is_valid(item)]
#
# temps = [12, -5, 0, -1, 18, -12]
#
# is_even = lambda x: x < 0
#
# result = filter_list(temps, is_even)
# print(result)

# def filter_list(data, condition):
#     return [item for item in data if condition(item)]
#
# a = [3, 4, 9, 10, 12, 7]
# b = [5, 8, 15, 20, 22]
#
# is_even = lambda x: x % 3 == 0
# is_odd = lambda x: x % 5 == 0
#
# result = filter_list(a, is_even) + filter_list(b, is_odd)
# print("Third list: ", result)

# def apply_to_all(data, operation):
#     return [operation(item) for item in data]
#
# #варіанти операцій
# square = lambda x: x ** 2              #квадрат
# duble = lambda x: x * 2                #подвоєння
# to_string = lambda x: f"Number {x}"    #перетворення в текст
# increment = lambda x: x + 1            #+1
#
# #list
# numbers = [1, 2, 3, 4, 5]
#
# #використання use
# print(apply_to_all(numbers, square))
# print(apply_to_all(numbers, duble))
# print(apply_to_all(numbers, to_string))
# print(apply_to_all(numbers, increment))

def transform_list(data, operation):
    return [operation(item) for item in data]

make_negative = lambda x: -x

numbers = [3, 8, 5, 10, 0]

negative_numbers = transform_list(numbers, make_negative)

print(f"Numbers: {negative_numbers}")