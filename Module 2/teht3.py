sk_kanteenn_pituus_input = input("Anna suorakulmion kannan: ")
sk_korkeus_input = input("Anna suorakulmion korkeuden: ")

sk_kanteenn_pituus = float(sk_kanteenn_pituus_input)
sk_korkeus = float(sk_korkeus_input)

print("Suorankulmion pinta-ala on: ", sk_korkeus*sk_kanteenn_pituus)
print("Suorankulmion piiri on: ", sk_korkeus*2 + sk_kanteenn_pituus*2)