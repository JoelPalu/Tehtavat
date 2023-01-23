def gallons(g):
    litre = g * 3.785
    return litre
user = float(input("Anna gallonamärän: "))

while user >= 0:
    print(f"{user} gallona on {gallons(user)} litraa ")
    user = float(input("Anna gallonamärän: "))