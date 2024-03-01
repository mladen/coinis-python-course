# Valjalo bi da sam umjesto G, K i B koristio hrast, kuca i blago, ali neka ga sad :)

x1 = int(input("Unesite x koordinatu starog hrasta: "))
y1 = int(input("Unesite y koordinatu starog hrasta: "))

x2 = int(input("Unesite x koordinatu stare kuce: "))
y2 = int(input("Unesite y koordinatu stare kuce: "))

G = (x1, y1)  # Pozicija starog hrasta
K = (x2, y2)  # Pozicija stare kuce
B = (x2 + 2, y2 - 3)  # Pozicija blaga

# Koordinate blaga
print("a) Koordinate blaga su: ", B)

# Vazdusno rastojanje izmedju starog hrasta i blaga
rastojanje_hrast_blago = ((G[0] - B[0]) ** 2 + (G[1] - B[1]) ** 2) ** 0.5
print(
    "b) Vazdusno rastojanje izmedju starog hrasta i blaga je: ", rastojanje_hrast_blago
)

# Rastojanje od hrasta do blaga, tako da moramo obici i kucu
rastojanje_hrast_blago_kuca = ((G[0] - B[0]) ** 2 + (G[1] - B[1]) ** 2) ** 0.5 + (
    (B[0] - K[0]) ** 2 + (B[1] - K[1]) ** 2
) ** 0.5
print(
    "c) Rastojanje od hrasta do blaga, tako da moramo obici i kucu je: ",
    rastojanje_hrast_blago_kuca,
)
