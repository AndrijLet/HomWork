print("Printing current and previous number sun in a range(10)")

previous_num = 0

for i in range(10):
    current_sum = i + previous_num
    print("Current number: ", i, "Previous number: ", previous_num, "Sum: ", sum)
    previous_num = i