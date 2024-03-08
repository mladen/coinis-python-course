broj = str(input("Unesite broj: "))

if broj.startswith("0b"):
    print("Uneseni broj je u binarnom obliku")
elif broj.startswith("0o"):
    print("Uneseni broj je u oktalnom obliku")
elif broj.startswith("0x"):
    print("Uneseni broj je u heksadecimalnom obliku")
else:
    print("Uneseni broj je u dekadnom obliku")
