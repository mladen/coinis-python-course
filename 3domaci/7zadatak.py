class Knjiga:
    def __init__(self, naslov, autor, godina_izdanja, broj_kopija):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja
        self.broj_kopija = broj_kopija

    # def __str__(self):
    #     return f"{self.naslov} - {self.autor}"

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

    # def obrisi_knjigu(self, knjiga) -> None:
    #     self.knjige.remove(knjiga)

    def obrisi_knjigu(self, naslov) -> None:
        for knjiga in self.knjige:
            if knjiga.get_naslov() == naslov:
                self.knjige.remove(knjiga)
                return
        print("Knjiga ne postoji")

    def pronadji_knjigu_po_naslovu(self, naslov) -> Knjiga:
        for knjiga in self.knjige:
            if knjiga.get_naslov() == naslov:
                return knjiga
        return None

    def pronadji_knjigu_po_autoru(self, autor) -> Knjiga:
        for knjiga in self.knjige:
            if knjiga.get_autor() == autor:
                return knjiga
        return None

    def pronadji_knjigu(self, naslov=None, autor=None) -> Knjiga:
        if naslov is not None:
            return self.pronadji_knjigu_po_naslovu(naslov)
        elif autor is not None:
            return self.pronadji_knjigu_po_autoru(autor)
        else:
            return None

    def iznajmi_knjigu(self, naslov=None, autor=None) -> None:
        knjiga = self.pronadji_knjigu(naslov, autor)
        if knjiga is not None:
            if knjiga.get_broj_kopija() > 0:
                knjiga.set_broj_kopija(knjiga.get_broj_kopija() - 1)
            else:
                print("Nema vise kopija knjige")
        else:
            print("Knjiga ne postoji")

    def vrati_knjigu(self, naslov=None, autor=None) -> None:
        knjiga = self.pronadji_knjigu(naslov, autor)
        if knjiga is not None:
            knjiga.set_broj_kopija(knjiga.get_broj_kopija() + 1)
        else:
            print("Knjiga ne postoji")


# knjiga1 = Knjiga("Rat i mir", "Lav Tolstoj", 1865, 2)
# knjiga2 = Knjiga("Zapisi iz podzemlja", "Fjodor Dostojevski", 1864, 3)
# knjiga3 = Knjiga("Zlocin i kazna", "Fjodor Dostojevski", 1866, 1)

# print(knjiga1.get_autor())
biblioteka1 = Biblioteka()

while True:
    print("\nIzaberite opciju:")
    print("1. Dodaj knjigu")
    print("2. Obrisi knjigu")
    print("3. Pronadji knjigu po naslovu")
    print("4. Pronadji knjigu po autoru")
    print("5. Iznajmi knjigu")
    print("6. Vrati knjigu")
    print("7. Prikazi sve knjige")
    print("8. Izlaz")
    izbor = input("Unesite broj opcije: ")

    if izbor == "1":
        naslov = input("Unesite naslov knjige: ")
        autor = input("Unesite autora knjige: ")
        godina_izdanja = int(input("Unesite godinu izdanja knjige: "))
        broj_kopija = int(input("Unesite broj kopija knjige: "))
        nova_knjiga = Knjiga(naslov, autor, godina_izdanja, broj_kopija)
        biblioteka1.dodaj_knjigu(nova_knjiga)
    elif izbor == "2":
        naslov = input("Unesite naslov knjige koju zelite da obrisete: ")
        biblioteka1.obrisi_knjigu(naslov)
    elif izbor == "3":
        naslov = input("Unesite naslov knjige koju zelite da pronadjete: ")
        knjiga = biblioteka1.pronadji_knjigu_po_naslovu(naslov)
        if knjiga is not None:
            print(
                f"Naslov: {knjiga.get_naslov()}, Autor: {knjiga.get_autor()}, Godina izdanja: {knjiga.get_godina_izdanja()}, Broj kopija: {knjiga.get_broj_kopija()}"
            )
        else:
            print("Knjiga ne postoji")
    elif izbor == "4":
        autor = input("Unesite autora knjige koju zelite da pronadjete: ")
        knjiga = biblioteka1.pronadji_knjigu_po_autoru(autor)
        if knjiga is not None:
            print(
                f"Naslov: {knjiga.get_naslov()}, Autor: {knjiga.get_autor()}, Godina izdanja: {knjiga.get_godina_izdanja()}, Broj kopija: {knjiga.get_broj_kopija()}"
            )
        else:
            print("Knjiga ne postoji")
    elif izbor == "5":
        naslov = input("Unesite naslov knjige koju zelite da iznajmite: ")
        biblioteka1.iznajmi_knjigu(naslov)
    elif izbor == "6":
        naslov = input("Unesite naslov knjige koju zelite da vratite: ")
        biblioteka1.vrati_knjigu(naslov)
    elif izbor == "7":
        print(biblioteka1)
    elif izbor == "8":
        break
