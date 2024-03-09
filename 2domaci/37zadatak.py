import random


def generisi_string():
    karakteri = ["0", "1", "*"]
    duzina = 3
    return "".join(random.choice(karakteri) for _ in range(duzina))


nasumicni_string = generisi_string()
print(nasumicni_string)
