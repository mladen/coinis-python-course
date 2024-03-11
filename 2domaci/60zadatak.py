start = 33
end = 46

brojevi = []
kvadrirani_brojevi = []

for i in range(start, end + 1):
    # print(i) # 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46
    if start % 3 == 0 and not start % 6 == 0:  # 33, 39, 45
        brojevi.append(start)
        kvadrirani_brojevi.append(i**2)

    start += 1

print(brojevi)
print(kvadrirani_brojevi)

print("Suma kvadriranih brojeva je:", sum(kvadrirani_brojevi))
