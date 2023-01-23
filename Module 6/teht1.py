def roll():
    import random

    value = random.randint(1,6)
    return(value)

status = True

while status == True:
    num = roll()
    print(num)
    if num == 6:
        status = False