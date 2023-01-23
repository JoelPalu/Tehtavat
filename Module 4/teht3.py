status = True
a = 0
list = []
while status == True:
    num = (input("Anna numero: "))
    if num != "":
        num = int(num)
        list.append(num)
        small = num
        large = num
    else: status = False

while a < len(list):
    num = list[a]
    if num <= small:
        small = num
    if num >= large:
        large = num
    a = a + 1

print(f"Isoin numero on: {large} ja pienin numero on: {small}")