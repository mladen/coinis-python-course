broj_slobodnih_sjedista_po_redu = [10, 8, 15, 12, 7]

broj_osoba = 8

# NOTE: Najvise mjesta ce ostati kada broj osoba u najslabije popunjenom redu saberemo sa broj_osoba. To je to, osim ako nesto nisam najbolje razumio :)
# U sustini, samo trebamo da nadjemo red u kojem ima najmanje ljudi.
print(f"Red u kojem ima najmanje ljudi je {min(broj_slobodnih_sjedista_po_redu)}")
