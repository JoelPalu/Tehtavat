list = []
total = 0
user = int(input("Anna luku: "))

for n in range(1,user):
    if user % n== 0:
        total = total + 1


if total <= 1:
    print(f"Luku {user} on alkuluku")
else: print(f"Luku {user} ei ole alkuluku")