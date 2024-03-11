list_plata = [600, 800, 1500, 1200, 900]

prosjecna_plata_u_evrima = sum(list_plata) / len(list_plata)

prosjecna_plata_u_dolarima = prosjecna_plata_u_evrima * 1.1

print("Prosjecna plata u EUR: ", prosjecna_plata_u_evrima)
print("Prosjecna plata u USD: ", prosjecna_plata_u_dolarima)
