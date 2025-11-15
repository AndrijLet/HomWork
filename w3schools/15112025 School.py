age = int(input("Enter your age: "))
if age <= 0 or age > 100:
    print("Invalid value")
elif age >= 18:
    print("You are old enough to vote!")
else:
    print("You are a minor")