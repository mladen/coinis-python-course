import os

cwd = os.getcwd()  # Get the current working directory (cwd)
file_path = os.path.join(cwd, "4domaci", "products.csv")

list_of_products = [
    {
        "naziv": "Televizor",
        "opis": "LG televizor 43inc",
        "godina": 2019,
        "kolicina": 10,
        "cijena": 300,
    },
    {
        "naziv": "Televizor",
        "opis": " Samsung televizor 39inc",
        "godina": 2017,
        "kolicina": 5,
        "cijena": 250,
    },
]


def append_to_file(list_of_products):
    try:
        with open(file_path, "a") as file:
            file.write("Naziv, Opis, Godina, Kolicina, Cijena\n")
            for product in list_of_products:
                file.write(
                    f"{product['naziv']}, {product['opis']}, {product['godina']}, {product['kolicina']}, {product['cijena']}\n"
                )
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Products successfully appended to file!")


append_to_file(list_of_products)
