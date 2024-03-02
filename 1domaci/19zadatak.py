def zbir_cifara(broj):
    jedinica = broj % 10
    desetica = broj // 10 % 10
    stotina = broj // 100
    return jedinica + desetica + stotina


trocifreni_broj = int(input("Unesite trocifreni broj: "))
print("Zbir cifara tog broja iznosi:", zbir_cifara(trocifreni_broj))
