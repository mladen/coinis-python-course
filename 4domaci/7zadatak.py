from functools import reduce

voce = ["apple", "banana", "apple", "orange", "banana", "apple"]


def fija(akumulator, voce):
    # print(akumulator, voce)
    if voce in akumulator:
        akumulator[voce] += 1
    else:
        akumulator[voce] = 1
    return akumulator


ponavljanje = reduce(fija, voce, {})
