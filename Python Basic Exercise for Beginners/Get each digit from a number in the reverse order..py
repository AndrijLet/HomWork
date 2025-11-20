number = 7536

while number > 0:
    last_digit = number % 10
    print(last_digit, end=" ")
    number = number // 10