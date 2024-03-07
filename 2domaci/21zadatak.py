import math

x = float(input("Unesite x: "))

if x <= -7:
    y = 2 * x + 7 / 2
elif x > -7 and x < 1:
    (x**2 - 3 * x + 5) / (x**2 + 2)
elif x >= 1 and x <= 8:
    y = math.sqrt(x**2 + 2 * x + 2) + (math.sqrt(abs((3 * x / 2) - 4 / 7)))
elif x > 8:
    y = abs((3 / x**2) - 11 * x)

print(f"y = {y}")
