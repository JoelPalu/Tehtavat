import random
user = int(input("Anna pisteiden määrä: "))
loop = 0
dots = 0

while loop != user:
    x = random.random()
    y = random.random()
    loop = loop + 1
    if x**2+y**2<1:
        dots = 1 + dots

print(4*dots/user)




