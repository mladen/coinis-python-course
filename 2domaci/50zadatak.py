# string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Sed auctor, libero nec lacinia tincidunt, nunc nunc tincidunt nunc, nec"
# string = "lasta"
string = "Recenica koja sadrzi slova i znakove interpunkcije."

novi_string = ""

for char in string:
    if char.lower() not in "aeiou,.":
        novi_string += char

print(novi_string)
