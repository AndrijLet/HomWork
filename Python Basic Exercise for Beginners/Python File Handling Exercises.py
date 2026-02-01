""" Read a File """
#
# try:
#     with open("sample.txt", 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: 'sample.txt' not found.")


"""Read File Line by Line"""

try:
    with open("sample.txt", 'r') as file:
        for line in file:
            print(line, end='') # The 'end=''' prevents extra newline characters
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")