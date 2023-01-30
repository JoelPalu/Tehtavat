def name_check(list, user):
    dublicate = False
    for n in list:
        if n == user:
            dublicate = True
    return dublicate

def haku(list):
    user_search = input("Anna lentokentän ICAO-koodi: ")
    if user_search in list:
        print(f"Lentokentän ICAO: {user_search} nimi on {ICAO[user_search]}")
    else:
        print("Annettua ICAO:ta ei löydy. Lisää sen kitjoittamalla ¨Uusi¨")

def uusi(list):
    user_search = input("Anna lentokentän ICAO-koodi: ")
    if name_check(list, user_search) == True:
        print(f"{user_search} on jo olemassa {list[user_search]}")
    else:
        new_ICAO, new_name = (user_search, input("Anna lentoaseman nimi: "))
        list[new_ICAO] = new_name
    return list


ICAO = {"EFHK":"Helsinki-Vantaan lentoasema",}

print("Haluatko hakea tai lisätä lentoaseman tai lopettaa? ")
user = input("Haku, Uusi, Lopeta: " )

while user != "Lopeta" and user != "lopeta":
    if user == "haku" or user == "Haku":
        haku(ICAO)
    elif user == "uusi" or user == "Uusi":
        ICAO = uusi(ICAO)
    else: print("Väärä syöte!")

    user = input("Haku, Uusi, Lopeta: ")