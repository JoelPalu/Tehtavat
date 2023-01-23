import random
total = 0
user = int(input("Monta arpakuutioita heitetän?: "))


for n in range(user):
    total = total + random.randint(1,6)

print(f"Heitetyn summa on: {total}")