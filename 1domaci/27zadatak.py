broj = int(input("Unesite cetvorocifreni broj: "))

# Izdvajanje cifara broja
hiljade = broj // 1000
stotine = (broj % 1000) // 100
desetice = (broj % 100) // 10
jedinice = broj % 10

zbir_cifara = hiljade + stotine + desetice + jedinice

kvadrat_zbira = zbir_cifara**2

print("Kvadrat zbira cifara datog broja je:", kvadrat_zbira)
