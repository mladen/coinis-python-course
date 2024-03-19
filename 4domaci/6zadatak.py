import random

# random_vremenska_serija = [random.randint(0, 100) for i in range(10)]
vremenska_serija = [0, 3, 4, 6, 8, 23, 45, 67, 89, 100]

# print(vremenska_serija)

# print(list(map(lambda x, y: y - x, vremenska_serija[:-1], vremenska_serija[1:])))
# za x imamo: vremenska_serija[:-1] = [0, 3, 4, 6, 8, 23, 45, 67, 89]
# za y imamo: vremenska_serija[1:] =  [3, 4, 6, 8, 23, 45, 67, 89, 100]
# Dakle, prvi niz ide od pocetka, a drugi od drugog elementa do kraja (dakle pomjeramo za jedno mesto u desno)

# drugi nacin
print(list(map(lambda x, y: y - x, vremenska_serija, vremenska_serija[1:])))
# za x imamo: vremenska_serija =  [0, 3, 4, 6, 8, 23, 45, 67, 89, 100]
# za y imamo: vremenska_serija[1:] = [3, 4, 6, 8, 23, 45, 67, 89, 100]
# Moze i samo ovako jer se ide do najmanjeg niza, a to je vremenska_serija[1:]
