num = input("Anna numero: ")

if num != "":
    small = int(num)
    large = int(num)

while num != "":
    num = input("Anna numero: ")
    if num != "":
        num= int(num)
        if num < large:

            large = num
        elif num > small:
            small = num
    else: print(f"Isoin numero on: {large} ja pienin numero on: {small}")

