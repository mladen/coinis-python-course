ucenici_i_prosjeci = {
    "Ivan": 4.5,
    "Marko": 3.5,
    "Janko": 5.0,
    "Petar": 4.0,
    "Milan": 1.0,
}

for ucenik in ucenici_i_prosjeci:
    # print(f"{ucenik}: {ucenici_i_prosjeci[ucenik]}")

    prosjek_trenutnog_ucenika = ucenici_i_prosjeci[ucenik]

    if prosjek_trenutnog_ucenika >= 4.5:
        print(f"{ucenik} je odlican ucenik.")
    elif prosjek_trenutnog_ucenika >= 3.5:
        print(f"{ucenik} je vrlo dobar ucenik.")
    elif prosjek_trenutnog_ucenika >= 2.5:
        print(f"{ucenik} je dobar ucenik.")
    elif prosjek_trenutnog_ucenika >= 2.0:
        print(f"{ucenik} je zadovoljavajuci ucenik.")
    else:
        print(f"{ucenik} je nezadovoljavajuci ucenik.")
