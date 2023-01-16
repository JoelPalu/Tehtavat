year = int(input("Ketsotaan, onko antama vuosi karkausvuosi. Kerro vuosi: "))
centry_check = float(year/100)
centry_check_int = int(centry_check)

if centry_check-centry_check_int == 0:
    centry_check = float(centry_check * 100 / 400)
    centry_check_int = int(centry_check)
    if centry_check-centry_check_int == 0:
        print(year,"on karkausvuosi")
    else: print(year,"ei ole karkausvuosi")
else:
    low_year = float(year / 4)
    low_year_int = int(low_year)
    if low_year - low_year_int == 0:
        print(year, "on karkausvuosi")
    else: print(year, "ei ole karkausvuosi")









