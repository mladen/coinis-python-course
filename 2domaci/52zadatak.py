# NOTE: Rjesenje ChatGPT-a
# def prosiri_string(a, pre, suf, num):
#     prosireni_string = pre + a + suf  # Dodajemo prefiks i sufiks originalnom stringu jednom
#     prosireni_string *= num  # Ponavljamo ovaj prosireni string num puta
#     return prosireni_string

# # Testiranje funkcije
# a = 'test'
# pre = 'pr'
# suf = 'su'
# num = 2

# rezultat = prosiri_string(a, pre, suf, num)
# print(rezultat)

# NOTE: Moje rjesenje
a = "test"
pre = "pr"
suf = "su"
num = 2

print(pre * num + a + suf * num)
