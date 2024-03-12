niz_cijelih_brojeva = [-2, 7, -5, 3, 1, -4]


def absolute_of_even_sum(niz):
    apsolutna_suma_parnih_elemenata = 0

    for broj in niz:
        if broj % 2 == 0 and broj < 0:
            apsolutna_suma_parnih_elemenata += abs(broj)

    print(apsolutna_suma_parnih_elemenata)


absolute_of_even_sum(niz_cijelih_brojeva)
