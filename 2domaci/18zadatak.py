trenutna_temperatura_vode = int(input("Unesi trenutnu temperaturu vode: "))

if trenutna_temperatura_vode <= 0:
    print("Cvrsto")
elif trenutna_temperatura_vode < 100:
    print("Tecno")
else:
    print("Gasovito")
