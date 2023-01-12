print("Lasken kolmen(3) luvun summan, tulon ja keskiarvon sulle!")

#Pyytää numerot
num1_input = input("Anna ensinmmäinen numero: ")
num2_input = input("Anna toinen numero: ")
num3_input = input("Anna kolmas numero: ")

#Muuttaa inputit numeroiksi
num1 = float(num1_input)
num2 = float(num2_input)
num3 = float(num3_input)

#Lasku menetelmät
print("Numeroiden summa on: ", num1 + num2 + num3)
print("Numeroiden tulo on: ", num1 * num2 * num3)
print("Numeroiden keskiarvo on: ", (num1 + num2 + num3)/3 )