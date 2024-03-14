def broj_ponavljanja(s):
    broj_poklapanja = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            broj_poklapanja += 1
            print("Poklapanje:", s[i], s[i + 1])
    return broj_poklapanja


string = "aabaaac"
print("Broj ponavljanja susjednih karaktera je:", broj_ponavljanja(string))
