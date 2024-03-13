def get_words_ends_with_letter(text, character):
    sentences = text.split(".")

    sentences = list(
        filter(lambda x: x != "", sentences)
    )  # Uklanja "recenice" koje ne sadrze nista

    print(sentences)

    result = []

    for sentence in sentences:
        words = sentence.split(" ")

        words = list(filter(lambda x: x != "", words))

        torka = ()
        for word in words:
            if word[-1] == character:
                torka = torka + (word,)

        torka += (len(torka),)  # Dodaje duzinu tuple-a na kraj tuple-a

        result.append(torka)

    print(result)


get_words_ends_with_letter(
    "Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences.",
    "s",
)
