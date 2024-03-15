class Knjiga:
    def __init__(self, naslov, autor, godina_izdanja, broj_kopija):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja
        self.broj_kopija = broj_kopija

    def __str__(self):
        return f"{self.naslov} - {self.autor}"

    def get_naslov(self) -> str:
        return self.naslov

    def set_naslov(self, novi_naslov) -> None:
        self.naslov = novi_naslov

    def get_autor(self) -> str:
        return self.autor

    def set_autor(self, novi_autor) -> None:
        self.autor = novi_autor

    def get_godina_izdanja(self) -> int:
        return self.godina_izdanja

    def set_godina_izdanja(self, nova_godina_izdanja) -> None:
        self.godina_izdanja = nova_godina_izdanja

    def get_broj_kopija(self) -> int:
        return self.broj_kopija

    def set_broj_kopija(self, novi_broj_kopija) -> None:
        self.broj_kopija = novi_broj_kopija


class Biblioteka:
    def __init__(self, knjige=None):
        self.knjige = [] if knjige is None else knjige

    def __str__(self):
        if not self.knjige:
            return "Biblioteka je prazna."
        else:
            rezultat = ""
            for knjiga in self.knjige:
                rezultat += f"Naslov: {knjiga.get_naslov()}, Autor: {knjiga.get_autor()}, Godina izdanja: {knjiga.get_godina_izdanja()}, Broj kopija: {knjiga.get_broj_kopija()}\n"
            return rezultat

    def get_knjige(self) -> list:
        return self.knjige

    # def set_knjige(self, nove_knjige) -> None:
    #     self.knjige = nove_knjige

    def dodaj_knjigu(self, nova_knjiga) -> None:
        self.knjige.append(nova_knjiga)

    def obrisi_knjigu(self, knjiga) -> None:
        self.knjige.remove(knjiga)

    def pronadji_knjigu(self, naslov) -> Knjiga:
        for knjiga in self.knjige:
            if knjiga.get_naslov() == naslov:
                return knjiga
        return None

    def iznajmi_knjigu(self, naslov) -> None:
        knjiga = self.pronadji_knjigu(naslov)
        if knjiga is not None:
            if knjiga.get_broj_kopija() > 0:
                knjiga.set_broj_kopija(knjiga.get_broj_kopija() - 1)
            else:
                print("Nema vise kopija knjige")
        else:
            print("Knjiga ne postoji")

    def vrati_knjigu(self, naslov) -> None:
        knjiga = self.pronadji_knjigu(naslov)
        if knjiga is not None:
            knjiga.set_broj_kopija(knjiga.get_broj_kopija() + 1)
        else:
            print("Knjiga ne postoji")


knjiga1 = Knjiga("Rat i mir", "Lav Tolstoj", 1865, 5)
knjiga2 = Knjiga("Zapisi iz podzemlja", "Fjodor Dostojevski", 1864, 5)
# print(knjiga1.get_autor())
biblioteka1 = Biblioteka()
biblioteka1.dodaj_knjigu(knjiga2)
biblioteka1.dodaj_knjigu(knjiga1)
# print(knjiga2)
# biblioteka1.dodaj_knjigu(knjiga2)
# print(biblioteka1)

for knjiga in biblioteka1.get_knjige():
    print(knjiga)
