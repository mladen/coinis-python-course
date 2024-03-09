string = str(input("Unesite strin koji sadrzi brojeve: "))
enkriptovani_string = ""

# lambda x: x in "0123456789"


def jeste_broj(c):
    return c in "0123456789"


for c in string:
    if jeste_broj(c):
        if int(c) % 2 == 0:
            enkriptovani_string += "0"
        else:
            enkriptovani_string += "1"
    else:  # za svaki slucaj da dodam i mogucnost da je korisnik unio nesto sto nije broj
        enkriptovani_string += c

print(enkriptovani_string)
