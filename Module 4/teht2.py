status = True
while status == True:
    inch = float(input("Anna tuuma määrän: "))
    if inch >= 0:
        print(f"{inch*2.54:1.2f}cm")
    else: status = False, print("False number")