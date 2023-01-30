kaudet = {1:"Talvi", 2:"Talvi",
          3:"Kevät", 4:"Kevät", 5:"Kevät",
          6:"Kesä", 7:"Kesä", 8:"Kesä",
          9:"Syksy", 10:"Syksy", 11:"Syksy", 12:"Talvi"}

user = int(input("Anna kuukeuden numero: "))
if user in kaudet:
    print(f"{user}. kuukauden kausi on {kaudet[user]}")