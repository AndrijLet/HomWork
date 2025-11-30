# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# list3 = []
#
# def numbers_od(list1, list2):
#     for number in list1:
#         if number % 2 != 0:
#             list3.append(number)
#     for number in list2:
#         if number % 2 == 0:
#             list3.append(number)
# numbers_od(list1, list2)
#
# print(list3)

#map(риймаємо функцію та масив)

# # for x in list1:
#
# def func(x):
#     return x
# new_arr = list(map())

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def numbers_od_clean(list1, list2):
    return [n for n in list1 if n % 2 !=0] + [n for n in list2 if n % 2 ==0]

list3 = numbers_od_clean(list1, list2)
print(list3)