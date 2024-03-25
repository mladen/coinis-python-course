import os
from pprint import pprint
from functools import reduce

# from functools import reduce

cwd = os.getcwd()  # Get the current working directory (cwd)
file_path = os.path.join(cwd, "4domaci", "cc_info.txt")

card_number = "4532 8756 1234 7678"


def credit_card_validation(card_number):
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16:
        return False
    if not card_number.isdigit():
        return False

    # print(f"Original card number: {card_number}\n")

    reversed_card_number = card_number[::-1]
    reversed_card_number_list = list(reversed_card_number)

    # print(f"Reversed car number list: {reversed_card_number_list}")

    every_second_number_doubled = [
        int(number) if index % 2 == 0 else int(number) * 2
        for index, number in enumerate(reversed_card_number_list)
    ]

    # print(f"Every second number doubled: {every_second_number_doubled}")

    every_second_number_clean = []
    for number in every_second_number_doubled:
        if number >= 10:
            number = int(str(number)[0]) + int(str(number)[1])
        # print(number)
        every_second_number_clean.append(number)

    # print(f"Every second number clean: {every_second_number_clean}")

    # print(f"Added and divided by 10: {sum(every_second_number_clean)/10}")

    if sum(every_second_number_clean) / 10 % 2 == 0:
        return True
    else:
        return False


# Checks one credit card
# print(credit_card_validation(card_number))

# Checks all the credit cards from file cc_info.txt
with open(file_path, "r") as file:
    for line in file:
        card_number = line.strip()
        print(
            f"Credit card {card_number} is a valid credit card: {credit_card_validation(card_number)}"
        )
