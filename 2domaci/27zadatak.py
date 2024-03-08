neki_string = "Pa i ovo je neki string"

for slovo in neki_string.lower():
    if slovo in "aeiou":
        print("Uneseni string sadrzi samoglasnike. Prvi na koji smo naisli je: ", slovo)
        break
    else:
        print("Uneseni string ne sadrzi samoglasnike")
