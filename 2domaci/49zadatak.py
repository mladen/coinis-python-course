# string = str(input("Unesite string: "))
string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
duzina = 10

if len(string) <= duzina:
    print(string + "...")
else:
    print(string[:duzina] + "...")
