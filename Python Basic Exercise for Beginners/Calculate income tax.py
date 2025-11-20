# income = 45000
# tax = 0
#
# if income <= 10000:
#     tax = 0
#
# elif income <= 20000:
#     tax = (income - 10000) * 0.10
#
# else:
#     tax = (10000 * 0.10)

def calculate_tax(income):
    if income < 10000:
        return 0
    elif income <= 20000:
        return (income - 10000) * 0.10
    else:
        return (10000 * 0.10) + (income - 20000) * 0.20

user_income = int(input("Enter your income: "))
tax = calculate_tax(user_income)

print(f"Your income is: ${tax}")
