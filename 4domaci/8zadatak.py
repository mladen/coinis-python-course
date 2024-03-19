from functools import reduce

pravougaonici = [[4, 3], [7, 2], [2, 2], [3, 5], [4, 4]]


def fija(akumulator, pravougaonik):
    if pravougaonik[0] == pravougaonik[1]:
        akumulator.append(pravougaonik)

    return akumulator


izdvojeni_kvadrati = reduce(fija, pravougaonici, [])
print(f"Izdvojeni kvadrati {izdvojeni_kvadrati}")


def najveci_kvadrat(akumulator, kvadrat):
    # print(akumulator, kvadrat)

    # Prvi nacin
    # if akumulator[0] < kvadrat[0]:
    #     akumulator = kvadrat
    # return akumulator

    # Drugi nacin
    return (
        kvadrat if akumulator[0] < kvadrat[0] else akumulator
    )  # Bilo sta sto se vraca ovdje, postaje novi akumulator (nova vrednost akumulatora)


print(reduce(najveci_kvadrat, izdvojeni_kvadrati, izdvojeni_kvadrati[0]))
