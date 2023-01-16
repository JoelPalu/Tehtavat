status = True
num = (input("Anna numero: "))
small = int(num)
large = int(num)

while status == True:
    num = (input("Anna numero: "))
    if num != "":
        num= int(num)
        if num < large:
            large = num
        elif num > small:
            small = num
    else: status = False

print(f"Isoin numero on: {large} ja pienin numero on: {small}")