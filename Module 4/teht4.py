import random
user = 0
num = random.randint(1,10)

while user != num:
    user = int(input("Arvaa numero 1 - 10: "))
    if user > num:
        print("Liian suuri arvaus")
    elif user < num:
        print("Liian pieni arvaus")

print(f"Oikein. Se oli {num}!")