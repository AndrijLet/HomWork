#accept a string from the user

user_str = input("Enter a string: ")

print("Original String is", user_str)
print("Printing only even index chars")

"""
цикл по кожному символу з парним індексом 
cycle for each sumbol with an even index
"""
for i in range(0, len(user_str), 2):
    print(user_str[i])