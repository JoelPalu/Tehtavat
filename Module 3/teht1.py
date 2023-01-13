catch = input("Kerro kuhan pituuden: " )
catch = float(catch)

if catch<37:
    print("Saalis on liian pieni, päätä takaisiin veteen. Kuha pitäisi olla", 37-catch, "cm pitempi!")

if catch>=37:
    print("Hyvä saalis! Voit viedä sen kottiin :D")