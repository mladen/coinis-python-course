string = "Ovo je neka recenica"
lista = string.split()

najduza_rijec = ""

for rijec in lista:
    if len(rijec) > len(najduza_rijec):
        najduza_rijec = rijec

print(f"Najduza rijec je '{najduza_rijec}'")
