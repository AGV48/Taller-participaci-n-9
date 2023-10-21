nombres_leidos: list[str] = []

with open("nombres.txt", "r") as archivo:
    for linea in archivo:
        nombres_leidos.append(linea.strip())
    
print("Los nombres leidos son: ", nombres_leidos)