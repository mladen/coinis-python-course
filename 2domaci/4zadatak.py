trenutno_vrijeme = int(input("Unesite trenutno vrijeme (sate): "))

if (
    trenutno_vrijeme < 6
    or (trenutno_vrijeme > 13 and trenutno_vrijeme < 17)
    or trenutno_vrijeme > 22
):
    print(
        "Ne mozete izvoditi radove trenutno. Sacekajte da prodje kucni red (13-17h, 22-06h)."
    )
else:
    print("Mozete izvoditi radove.")
