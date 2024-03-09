string = str(input("Unesite recenicu tako da sva slova budu mala: "))

novi_string = ""

for i in range(len(string)):
    if string[i] in "aeiou":
        novi_string += "1"
    else:
        novi_string += "0"

print(novi_string)  # Npr. za s = "abaae" rezultat je 10111
