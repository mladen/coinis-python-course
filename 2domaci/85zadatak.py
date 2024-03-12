# ---++++---
# --+++-----
lista_slobodnih_sjedista_po_redovima = [7, 6, 8, 3, 2, 4, 3, 7]

# Da bismo zauzeli sto manji broj redova, iskoristicemo redove koji imaju najvise slobodnih mjesta.
# Zato cemo sortirati lista_slobodnih_sjedista_po_redovima i krenuti od tih redova koji su najmanje popunjeni.
sortirana_lista_slobodnih_sjedista_po_redovima = sorted(
    lista_slobodnih_sjedista_po_redovima
)[::-1]
print(
    f"Sortirana lista slobodnih sjedista po redovima je: ",
    sortirana_lista_slobodnih_sjedista_po_redovima,
)

broj_posjetilaca = 15  # Broj novih posjetilaca
broj_potrebnih_mjesta = []
broj_redova = 0

for red in range(len(sortirana_lista_slobodnih_sjedista_po_redovima)):
    broj_slobodnih_sjedista_u_redu = sortirana_lista_slobodnih_sjedista_po_redovima[red]
    print(broj_slobodnih_sjedista_u_redu)

    broj_potrebnih_mjesta.append(broj_slobodnih_sjedista_u_redu)
    broj_redova += 1

    if broj_posjetilaca <= sum(broj_potrebnih_mjesta):
        break

print(
    f"Najmanji broj redova koje trebamo da rezervisemo je {broj_redova}, a broj potrebnih mjesta je {broj_potrebnih_mjesta}."
)  # Za broj potrebnih redova mozemo uzeti i len(broj_potrebnih_mjesta)
