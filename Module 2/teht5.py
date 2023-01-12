luoti = 13.3
naula = 32*luoti
leiviska = 20*naula

leiviska_input = input("Anna leiviskä määrä: ")
naula_input = input("Anna naula määrä: ")
luoti_input = input("Anna luoti määrä: ")

leiviska_maara = int(leiviska_input)
naula_maara = int(naula_input)
luoti_maara = int(luoti_input)


#kokonais paino grammoinna
total_weight = leiviska_maara*leiviska + naula_maara*naula + luoti_maara*luoti

#Lasketan kilot ja grammat erilleen
kilogramms = int(f"{total_weight / 1000 :10.0f}")
gramms = float(f"{total_weight-kilogramms*1000:.5f}")

print(f"Kokonainen massa on: {kilogramms} kilogrammaa ja {gramms} grammaa" )
