print("Laivalla on tarjolla 4 hyttiluokkaa: LUX, A, B ja C")

user_input = input("Kerro mistä hyttiluokasta haluaisit saada tietoa: ")

if user_input == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif user_input == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif user_input == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif user_input =="C":
    print("C on ikkunaton hytti autokannen alapuolella.")

else :
    print("Virheellinen hyttiluokka. Tarjolla on: LUX, A, B ja C")

