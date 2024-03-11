# lozinka = "1032asdakl23@#"
lozinka = "32135443"
lozinka = "3213544aA"

if len(lozinka) < 8:
    print("Lozinka mora imati bar 8 karaktera")
elif not any(char.isdigit() for char in lozinka):
    print("Lozinka mora imati bar jedan broj")
elif not any(char.isalpha() and char.islower() for char in lozinka):
    print("Lozinka mora imati bar jedno malo slovo")
elif not any(char.isalpha() and char.isupper() for char in lozinka):
    print("Lozinka mora imati bar jedno veliko slovo")
