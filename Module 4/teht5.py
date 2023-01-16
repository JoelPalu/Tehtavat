the_user = "python"
the_password = "rules"
total_tries = 5
tries = 0
status= False
end = "Block"


while status != True:
    while tries != 5:
        user = input("Anna käyttäjätunnus: ")
        password = input("Anna salasana: ")
        if user != the_user:
            print("Käyttäjätunnus tai salasana on väärin.")
            tries = tries + 1
        elif password != the_password:
            print("Käyttäjätunnus tai salasana on väärin.")
            tries = tries + 1
        else:
            status = True
            end = "Pass"
            tries = 5
    if status == False:
        status = True
        end = "Block"

if end == "Pass":
    print("Tervetuloa!")
else: print("Pääsy evätty")


