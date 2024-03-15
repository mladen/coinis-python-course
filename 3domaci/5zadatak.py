podkasti = [
    {"naziv": "Español para principiantes", "br_pozitivni": 1000, "br_negativni": 10},
    {"naziv": "Philophize This!", "br_pozitivni": 500, "br_negativni": 30},
    {"naziv": "Science VS. ", "br_pozitivni": 200, "br_negativni": 30},
]


def najlosiji_podkast(podkasti):
    najlosiji = podkasti[0]

    for podkast in podkasti:
        if (
            podkast["br_pozitivni"] / podkast["br_negativni"]
            < najlosiji["br_pozitivni"] / najlosiji["br_negativni"]
        ):
            najlosiji = podkast
    return {
        "najlosiji_podkast": najlosiji["naziv"],
        "odnos": najlosiji["br_pozitivni"] / najlosiji["br_negativni"],
    }


rezultat = najlosiji_podkast(podkasti)
# print(type(rezultat))
print(
    f"Najlosiji podkast je \"{rezultat['najlosiji_podkast']}\" a odnos dobrih naspram losih komentara je {round(rezultat['odnos'], 2)}"
)
