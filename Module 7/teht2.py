def name_check(list, user):
    dublicate = False
    for n in list:
        if n == user:
            dublicate = True
    return dublicate


nimet = set()

user = input("Anna nimi: ")

while user != "":
    if False == name_check(nimet, user):
        nimet.add(user)
        print("Uusi nimi")
    else: print("Aiemmin syötetty nimi")
    user = input("Anna nimi: ")

print(nimet)