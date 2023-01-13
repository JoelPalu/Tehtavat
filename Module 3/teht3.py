print("Katsotaan onko sinun hemoglobiiniarvot kunnossa.")

sex = input("Kerro sukupoli. M tai N: ")
arvo = float(input("Kerro hemoglobiiniarvo: "))

if sex == "M":
    if arvo<134:
        print("Hemoglobiiniarvo on matala. Normaali on 134-195 g/l.")
    elif arvo>195:
        print("Hemoglobiiniarvo on korkea. Normaali on 134-195 g/l.")
    else: print("Hemoglobiiniarvo on normaali.")

if sex == "N":
    if arvo<117:
        print("Hemoglobiiniarvo on matala. Normaali on 117-175 g/l.")
    elif arvo>175:
        print("Hemoglobiiniarvo on korkea. Normaali on 117-175 g/l.")
    else: print("Hemoglobiiniarvo on normaali.")