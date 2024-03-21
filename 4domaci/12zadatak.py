import os
from pprint import pprint
from functools import reduce

# from functools import reduce

cwd = os.getcwd()  # Get the current working directory (cwd)
file_path = os.path.join(cwd, "4domaci", "brojevi.txt")

try:
    with open(file_path, "r") as file:
        read_content = file.read()
        print(read_content)

        print("\n")

        # Jedan nacin
        # heksadecimalni_brojevi = [
        #     red for red in read_content.split("\n") if red.startswith("0x")
        # ]

        # Drugi nacin (funkcionalni)
        heksadecimalni_brojevi = list(
            filter(lambda red: red.startswith("0x"), read_content.split("\n"))
        )

        # Jedan nacin
        # decimalni_brojevi = [int(broj, 16) for broj in heksadecimalni_brojevi]

        # Drugi nacin (funkcionalni)
        decimalni_brojevi = list(
            map(lambda broj: int(broj, 16), heksadecimalni_brojevi)
        )
        print(f"Dekadni brojevi su: {list(decimalni_brojevi)}\n\n")

        suma_brojeva_sa_zadnjom_cifrom_tri = reduce(
            lambda suma_akumulator, broj: (
                # Prvi nacin
                suma_akumulator + broj
                if broj % 10 == 3
                else suma_akumulator
                # Drugi nacin
                # suma_akumulator + int(broj)
                # if str(broj)[-1] == "3"
                # else suma_akumulator
            ),
            decimalni_brojevi,
            0,
        )
        print(
            f"Suma brojeva koji se zavrsavaju brojem 3 je {suma_brojeva_sa_zadnjom_cifrom_tri}."
        )


except FileNotFoundError:
    print("Fajl nije pronadjen")
except Exception as e:
    print(f"Doslo je do greske: {e}")
