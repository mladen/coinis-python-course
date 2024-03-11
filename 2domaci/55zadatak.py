# NOTE: Copilot-ovo rjesenje (dobro, ali tesko razumljivo)
# h = 8
# o = 3

# broj_molekula_vode = min(h // 2, o)
# print(f"Mozemo da imamo najvise {broj_molekula_vode}")

# NOTE: Moje rjesenje
h = 4
o = 3
broj_molekula_vode = 0

broj_potrebnih_molekula_vodonika = h // 2

if broj_potrebnih_molekula_vodonika <= o:
    broj_molekula_vode = broj_potrebnih_molekula_vodonika
else:
    broj_molekula_vode = o
print(f"Mozemo da imamo najvise {broj_molekula_vode}")
