a = float(input("Unesite duzinu jedne stranice trougla: "))
b = float(input("Unesite duzinu druge stranice trougla: "))
c = float(input("Unesite duzinu trece stranice trougla: "))

if a + b > c and a + c > b and b + c > a:
    print("Trougao je moguce konstruisati.")
else:
    print("Trougao nije moguce konstruisati.")
