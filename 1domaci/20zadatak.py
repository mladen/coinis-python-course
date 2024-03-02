def rastavi_na_cifre(broj):
    jedinica = broj % 10
    desetica = broj // 10 % 10
    stotina = broj // 100
    return stotina, desetica, jedinica


trocifreni_broj = int(input("Unesite trocifreni broj: "))

jedinica, desetica, stotina = rastavi_na_cifre(trocifreni_broj)

proizvod_cifara = jedinica * desetica * stotina
zbir_cifara = jedinica + desetica + stotina

print(
    "Razlika proizvoda i zbira cifara tog broja iznosi:", proizvod_cifara - zbir_cifara
)
