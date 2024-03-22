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


# Writes the list of products to a file
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


# Reads the products from the file and prints the ones older than the given year
def get_products_older_than(year):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines[1:]:  # Skip the first line
                product = line.strip().split(", ")
                if int(product[2]) > year:
                    print(product)
    except Exception as e:
        print(f"An error occurred: {e}")


get_products_older_than(2018)


# Reads the products from the file and prints the price of all the products
def get_total_price():
    total_price = 0
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines[1:]:  # Skip the first line
                product = line.strip().split(", ")
                total_price += int(product[3]) * int(product[4])
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The total price of all products is: {total_price}")


get_total_price()
