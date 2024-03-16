import random


class Turnir:
    def __init__(self, naziv_turnira, broj_rundi):
        self._naziv_turnira = naziv_turnira
        self._lista_igraca = []
        self._broj_rundi = broj_rundi

    def __str__(self):
        if not self._lista_igraca:
            return "Lista igraca je prazna."
        else:
            rezultat = ""
            for igrac in self._lista_igraca:
                rezultat += f"Igrac: {igrac[0]}, poeni igraca {igrac[1]}\n"
            return rezultat

    def get_naziv_turnira(self):
        return self._naziv_turnira

    def set_naziv_turnira(self, naziv_turnira):
        self._naziv_turnira = naziv_turnira

    def get_lista_igraca(self):
        return self._lista_igraca

    def set_lista_igraca(self, lista_igraca):
        self._lista_igraca = lista_igraca

    def get_broj_rundi(self):
        return self._broj_rundi

    def set_broj_rundi(self, broj_rundi):
        if 0 < broj_rundi < 10:  # Ogranicenje broja rundi; mora biti izmedju 0 i 10
            self._broj_rundi = broj_rundi
        else:
            raise ValueError("Broj rundi mora biti veci od 0 i manji od 10.")

    def dodaj_igraca(self, ime_igraca):
        self._lista_igraca.append((ime_igraca, 0))

    def obrisi_igraca(self, ime_igraca):
        for igrac in self._lista_igraca:
            if igrac[0] == ime_igraca:
                self._lista_igraca.remove(igrac)
                return
        print("Igrac sa unesenim imenom nije pronadjen.")

    def prikazi_najboljeg_igraca(self):
        if not self._lista_igraca:
            print("Lista igraca je prazna.")
            return
        najbolji_igrac = max(
            self._lista_igraca, key=lambda x: x[1]
        )  # Kao kljuc koristimo lambda funkciju koja vraca drugi element tuple-a
        print("Najbolji igrac:", najbolji_igrac[0])

    def pokreni_rundu(self):
        if len(self._lista_igraca) < 2:
            print("Nedovoljno igraca za pokretanje runde.")
            return

        slucajno_izabrani_igrac_1, slucajno_izabrani_igrac_2 = random.sample(
            self._lista_igraca, 2
        )
        print(
            f"Izabrao sam igrace: {slucajno_izabrani_igrac_1[0]} i {slucajno_izabrani_igrac_2[0]}."
        )

        rezultat = random.random()
        if rezultat <= 0.6:
            pobjednik = slucajno_izabrani_igrac_1
            gubitnik = slucajno_izabrani_igrac_2
        else:
            pobjednik = slucajno_izabrani_igrac_2
            gubitnik = slucajno_izabrani_igrac_1

        # Update-ujemo listu igraca i njihove poene
        self._lista_igraca.remove(pobjednik)
        self._lista_igraca.remove(gubitnik)
        pobjednik = (pobjednik[0], pobjednik[1] + 1)
        self._lista_igraca.append(pobjednik)
        self._lista_igraca.append(gubitnik)

        print(
            f"Igraci u ovoj rundi: {slucajno_izabrani_igrac_1[0]} i {slucajno_izabrani_igrac_2[0]}. Pobjednik je {pobjednik[0]}.\n"
        )
        self._broj_rundi += 1


turnir = Turnir("Teniski turnir", 5)
turnir.dodaj_igraca("Igrac 1")
turnir.dodaj_igraca("Igrac 2")
turnir.dodaj_igraca("Igrac 3")
print(f"\nTrenutna lista igraca i njihovih poena:\n{turnir}")
turnir.pokreni_rundu()
turnir.pokreni_rundu()
turnir.pokreni_rundu()
print(f"\nTrenutna lista igraca i njihovih poena:\n{turnir}")
turnir.prikazi_najboljeg_igraca()
