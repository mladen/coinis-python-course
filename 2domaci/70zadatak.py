lista_brojeva = [3, 6, 9, 21, 41, 51, 7]  # 9, 36, 81, 441, 2601
zbir_kvadrata = 0

for broj in lista_brojeva:
    if broj % 3 == 0:
        zbir_kvadrata += broj**2

print("Zbir kvadrata brojeva koji su djeljivi sa tri je: ", zbir_kvadrata)
