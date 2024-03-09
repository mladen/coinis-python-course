segment_start = int(input("Unesite pocetni broj: "))  # Npr. 2
segment_end = int(input("Unesite krajnji broj: "))  # Npr. 10

for i in range(segment_start, segment_end + 1):
    if (
        i % 2 == 0
        and i % 4 != 0  # Ovo znaci da je broj deljiv sa 2, ali nije deljiv sa 4
    ):
        print(i)
