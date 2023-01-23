def summ(list):
    total = 0
    list2 = []
    for n in list:
        if n%2 == 0:
            list2.append(n)
    return list2

list = []
user = input("Anna luku: ")
while user != "":
    list.append(int(user))
    user = input("Anna luku: ")

print(summ(list))
print(list)
