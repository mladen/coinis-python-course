# NOTE: Rjesenje ChatGPT-a
# def provjeri_jaku_lozinku(lozinka):
#     # Provjera duzine lozinke
#     if len(lozinka) < 8:
#         return "NO"

#     # Provjera postojanja malih slova, velikih slova i cifara u lozinci
#     ima_mala_slova = any(c.islower() for c in lozinka)
#     ima_velika_slova = any(c.isupper() for c in lozinka)
#     ima_cifre = any(c.isdigit() for c in lozinka)

#     # Ako su ispunjeni svi uslovi, lozinka je jaka
#     if ima_mala_slova and ima_velika_slova and ima_cifre:
#         return "YES"
#     else:
#         return "NO"

# # Unos lozinke od korisnika
# lozinka = input("Unesite lozinku: ")

# # Provjera da li je lozinka jaka i ispis rezultata
# print("Da li je lozinka jaka:", provjeri_jaku_lozinku(lozinka))

# NOTE: Moje rjesenje
# lozinka = "1032asdakl23@#"
lozinka = "32135443"
lozinka = "3213544aA"

if len(lozinka) < 8:
    print("Lozinka mora imati bar 8 karaktera")
elif not any(char.isdigit() for char in lozinka):
    print("Lozinka mora imati bar jedan broj")
elif not any(char.isalpha() and char.islower() for char in lozinka):
    print("Lozinka mora imati bar jedno malo slovo")
elif not any(char.isalpha() and char.isupper() for char in lozinka):
    print("Lozinka mora imati bar jedno veliko slovo")
