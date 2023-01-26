def pizza_worth(size,prise):
    import math


    m2 = size/1000 * math.pi
    worth = prise/m2
    return worth


while True:
    ps1 = float(input("Anna pizza 1 halkasija cm: "))
    pp1 = float(input("Anna pizza 1 hinta €: "))
    ps2 = float(input("Anna pizza 2 halkasija cm: "))
    pp2 = float(input("Anna pizza 2 hinta €: "))
    if pizza_worth(ps1,pp1) > pizza_worth(ps2,pp2):
        print(f"Pizza 2 {pizza_worth(ps2,pp2):1.2f} €/m2 on enemmän worth ku pizza 1 {pizza_worth(ps1,pp1):1.2f} €/m2")
    elif pizza_worth(ps1,pp1) < pizza_worth(ps2,pp2):
        print(f"Pizza 1 {pizza_worth(ps1, pp1):1.2f} €/m2 on enemmän worth ku pizza 2 {pizza_worth(ps2, pp2):1.2f} €/m2")
    else: print(f"Pizzat ovat yhtä suuret hinnoiltaan. {pizza_worth(ps1, pp1):1.2f} €/m2 ")