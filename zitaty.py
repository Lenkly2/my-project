with open("saves.txt","r") as file:
    data = file.read()
    print(data)

vopros = input("Бажаєте додати цитату?")

while vopros != "Ні":

    zitata = input("Введіть цитату")
    aftor = input("Введіть автора")

    with open("saves.txt","a") as file:
        file.write(zitata)
        file.write(aftor)
    vopros = input("Бажаєте додати цитату?")
with open("saves.txt","r") as file:
    data = file.read()
    print(data)
