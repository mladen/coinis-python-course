class Televizor:
    def __init__(
        self, broj_tekuceg_kanala, naziv_tekuceg_kanala, jacina_tona, kanali=[]
    ):
        self.broj_tekuceg_kanala = broj_tekuceg_kanala  # int (1 i 10)
        self.naziv_tekuceg_kanala = naziv_tekuceg_kanala
        self.jacina_tona = jacina_tona  # int (izmedju 0 i 10)
        self.kanali = kanali  # Lista kanala

    # Geteri i seteri
    def get_broj_tekuceg_kanala(self) -> int:
        return self.broj_tekuceg_kanala

    def set_broj_tekuceg_kanala(self, broj_tekuceg_kanala) -> None:
        if (
            broj_tekuceg_kanala < 1 or broj_tekuceg_kanala > 10
        ):  # Ako je broj kanala manji od 1 ili veci od 10
            print("Broj kanala mora biti izmedju 1 i 10")
            return
        self.broj_tekuceg_kanala = broj_tekuceg_kanala

    def get_naziv_tekuceg_kanala(self) -> str:
        return self.naziv_tekuceg_kanala

    def set_naziv_tekuceg_kanala(self, naziv_tekuceg_kanala) -> None:
        self.naziv_tekuceg_kanala = naziv_tekuceg_kanala

    def get_jacina_tona(self) -> int:
        return self.jacina_tona

    def set_jacina_tona(self, jacina_tona) -> None:
        if (
            jacina_tona < 0 or jacina_tona > 10
        ):  # Ako je jacina tona manja od 0 ili veca od 10
            print("Jacina tona mora biti izmedju 0 i 10")
            return
        self.jacina_tona = jacina_tona

    def get_kanali(self) -> list:
        return self.kanali

    def set_kanali(self, kanali) -> None:
        self.kanali = kanali


mladen_gleda = Televizor(1, "Prva", 5)
print("Mladen gleda: ", mladen_gleda.get_broj_tekuceg_kanala())

mladen_gleda.set_broj_tekuceg_kanala(99)
print("Mladen gleda: ", mladen_gleda.get_broj_tekuceg_kanala())
