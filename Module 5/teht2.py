list = []
user = input("Anna luku: ")

while user != "":
    list.append(int(user))
    user = input("Anna luku: ")

list.sort(reverse = True)
print(list[0:5])