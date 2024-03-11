string = "15023"
enkriptovani_string = ""

for char in string:
    if int(char) % 2 == 0:
        enkriptovani_string += "0"
        # print(f"{char} je paran broj - postavi 0")
    else:
        enkriptovani_string += "1"
        # print(f"{char} je neparan broj - postavi 1")

print(enkriptovani_string)
