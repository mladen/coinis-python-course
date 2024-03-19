import os

# from functools import reduce

cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

grad_koji_je_korisnik_izabrao = str(input("Unesite ime grada: "))

with open(cwd + "/4domaci/cities.txt", "r") as file:
    read_content = file.read()
    print(read_content)

    print("\n")

    svi_podaci = [red.split(",") for red in read_content.split("\n")]
    print(svi_podaci)

    izabrani_grad_i_okolina = list(
        filter(lambda grad: grad[0] == grad_koji_je_korisnik_izabrao, svi_podaci)
    )
    print(f"\n\nIzabrani grad, njegovi dijelovi i okolina: {izabrani_grad_i_okolina}")

    # sorting data by the last item in a sublist
    grad_sortirano = sorted(
        izabrani_grad_i_okolina, key=lambda x: int(x[2]), reverse=True
    )
    print(f"Dio grada sa najvecim brojem stanovnika je {grad_sortirano[0][1]}")
