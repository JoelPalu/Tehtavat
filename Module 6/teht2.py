def roll(sides):
    import random

    value = random.randint(1,sides)
    return(value)

user= int(input("Anna maksimi silmäluku: "))
status = True

while status == True:
    num = roll(user)
    print(num)
    if num == user:
        status = False