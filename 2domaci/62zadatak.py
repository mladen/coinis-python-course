string = "12 0x1A 0001 121 0x2"
# string = "12 001 31"

string_u_listu = string.split()
nova_lista = []

for str in string_u_listu:
    if str.startswith("0x"):
        print(str)
        nova_lista.append(str)

print("Broj heksadecimalnih brojeva je: ", len(nova_lista))
