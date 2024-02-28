import math

# def broj_litara_vode(vrijeme):
#     litara = (
#         vrijeme / 2
#     )
#     return math.floor(litara)

# broj_litara_vode kao lambda funkcija
broj_litara_vode = lambda vrijeme: math.floor(
    vrijeme / 2
)  # 1 sat voznje = 0.5 litara vode; 11.8 sati voznje = 5.9 litara vode

vrijeme = float(input("Unesite vrijeme voznje bicikla u satima: "))
litara = broj_litara_vode(vrijeme)
print("Marko će popiti {} litara vode.".format(litara))
