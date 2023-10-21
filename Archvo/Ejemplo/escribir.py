nombres: list[str] = ["Gabriel", "Jaime", "Diego", "Eliana", "Daniela"]

with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")