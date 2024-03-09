# def razlika_u_zaradi(originalne_cene, nove_cene):
#     # Proizvodimo listu razlika u cenama za svaki proizvod
#     razlike = [
#         originalna - nova for originalna, nova in zip(originalne_cene, nove_cene)
#     ]

#     # Sabiramo sve razlike kako bismo dobili ukupnu razliku u zaradi
#     ukupna_razlika = sum(razlike)

#     return ukupna_razlika


# # Primer
# originalne_cene = [100, 200, 150, 300]
# nove_cene = [90, 180, 135, 270]

# razlika = razlika_u_zaradi(originalne_cene, nove_cene)
# print("Ukupna razlika u zaradi:", razlika)


def razlika_u_zaradi(originalne_cijene, nove_cijene):
    ukupna_razlika = 0
    for i in range(len(originalne_cijene)):
        ukupna_razlika += originalne_cijene[i] - nove_cijene[i]
    return ukupna_razlika


originalne_cijene = [100, 200, 150, 300]
nove_cijene = [90, 180, 135, 270]

razlika = razlika_u_zaradi(originalne_cijene, nove_cijene)
print("Ukupna razlika u zaradi:", razlika)
