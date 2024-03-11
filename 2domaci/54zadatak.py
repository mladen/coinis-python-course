string = "01010"

# pozicija = 1  # prvi karakter u stringu
pozicija = 3  # srednji karakter u stringu
# pozicija = 5  # poslednji karakter u stringu


def slobodno_nije_slobodno(vrijednost_polja):
    print("Slobodno" if vrijednost_polja == "0" else "Nije slobodno")


if pozicija == 1:
    vrijednost_na_desnoj_poziciji = string[pozicija]
    # print(
    #     f"Vrijednost na desnoj poziciji, od pozicije {pozicija} (prvi karakter u stringu), je {vrijednost_na_desnoj_poziciji}"
    # )
    slobodno_nije_slobodno(vrijednost_na_desnoj_poziciji)
elif pozicija == len(string):
    vrijednost_na_lijevoj_poziciji = string[pozicija - 2]
    # print(
    #     f"Vrijednost na lijevoj poziciji, od pozicije {pozicija} (poslenji karakter u stringu), je {vrijednost_na_lijevoj_poziciji}"
    # )
    slobodno_nije_slobodno(vrijednost_na_lijevoj_poziciji)
else:
    vrijednost_na_desnoj_poziciji = string[pozicija]
    # print(
    #     f"Vrijednost na desnoj poziciji, od pozicije {pozicija}, je {vrijednost_na_desnoj_poziciji}"
    # )
    slobodno_nije_slobodno(vrijednost_na_desnoj_poziciji)

    vrijednost_na_lijevoj_poziciji = string[pozicija - 2]
    # print(
    #     f"Vrijednost na lijevoj poziciji, od pozicije {pozicija}, je {vrijednost_na_lijevoj_poziciji}"
    # )
    slobodno_nije_slobodno(vrijednost_na_lijevoj_poziciji)
