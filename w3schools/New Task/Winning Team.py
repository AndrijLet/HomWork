# Отримуємо бали для команди Apples

apple_3 = int(input()) * 3
apple_2 = int(input()) * 2
apple_1 = int(input())
apple_total = apple_1 + apple_2 + apple_3

# Отримуємо бали для команди Bananas
banana_3 = int(input()) * 3
banana_2 = int(input()) * 2
banana_1 = int(input())
banana_total = banana_1 + banana_2 + banana_3

if apple_total > banana_total:
    print("A")

elif banana_total > apple_total:
    print("B")

else:
    print("T")