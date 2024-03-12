cijene_aranzmana = [350, 450, 300, 600, 750]

budzet = 680
najskuplji_moguci_aranzman = 0

for aranzman in cijene_aranzmana:
    if aranzman > najskuplji_moguci_aranzman and aranzman <= budzet:
        najskuplji_moguci_aranzman = aranzman

print(f"Aranzman koji biram je onaj od {najskuplji_moguci_aranzman} EUR.")
print(f"Nakon ulozenog novca mi ostaje {budzet - najskuplji_moguci_aranzman}")
