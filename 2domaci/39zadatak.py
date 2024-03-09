broj = 153  # 1634

novi_broj = 0

for cifra in str(broj):
    novi_broj += int(cifra) ** len(str(broj))

if novi_broj == broj:
    print("Da. Broj je narcis.")
else:
    print("Ne. Broj nije narcis.")
