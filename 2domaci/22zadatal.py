koordinate_tacke = (
    int(input("Unesi x koordinatu tacke: ")),
    int(input("Unesi y koordinatu tacke: ")),
)

if koordinate_tacke[0] > 0 and koordinate_tacke[1] > 0:
    print("Tacka se nalazi u prvom kvadrantu")
elif koordinate_tacke[0] < 0 and koordinate_tacke[1] > 0:
    print("Tacka se nalazi u drugom kvadrantu")
elif koordinate_tacke[0] < 0 and koordinate_tacke[1] < 0:
    print("Tacka se nalazi u trecem kvadrantu")
elif koordinate_tacke[0] > 0 and koordinate_tacke[1] < 0:
    print("Tacka se nalazi u cetvrtom kvadrantu")
