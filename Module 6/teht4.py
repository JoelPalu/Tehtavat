def summ(list):
    total = 0
    for n in list:
        total = total + n
    return total

list = []
user = input("Anna luku: ")
while user != "":
    list.append(int(user))
    user = input("Anna luku: ")

print(summ(list))
