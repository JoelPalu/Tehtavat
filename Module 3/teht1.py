catch = float(input("Kerro kuhan pituuden: " ))

if catch<37:
    print("Saalis on liian pieni, päätä takaisiin veteen. Kuha pitäisi olla", 37-catch, "cm pitempi!")
else:
    print("Hyvä saalis! Voit viedä sen kottiin :D")