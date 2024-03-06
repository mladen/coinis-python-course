koordinate_pcele = (
    int(input("Unesi x koordinatu pcele: ")),
    int(input("Unesi y koordinatu pcele: ")),
)

# print(type(koordinate_pcele))

if koordinate_pcele[1] == 2 * koordinate_pcele[0] + 5:
    print("Pcela se krece po zici")
else:
    print("Pcela se ne krece po zici")
