#   Introduceți de la keyboarda o rată medie de creștere a populației
# Terrei calculați după câți ani față de 1992 se va dubla populația.
# (În 1992 Terra avea o populație de 5480 milioane de locuitori).
#   Exemplu.Dacă rata de creştere este de 0.05 (adică 58 pe an) atunci 
# populația se dublează în 15 ani.

def cati_ani(rata_de_crestere: float, pop:float = 5480, ani:int = 0) -> int:
    if pop >= 2 * 5480:
       return ani
    else:
        cati_ani(rata_de_crestere, pop + pop * rata_de_crestere, ani + 1)

#assert cati_ani(0.05) == 15, "Wrong answer"

def cand_x2_pop_terra_1992(rata_de_crestere):
    print("Daca rata de crestere a populatiei terrei este", rata_de_crestere,
    "atunci populatia terrei va fi dublul celei din 1992 dupa", cati_ani(rata_de_crestere), "ani.")


cand_x2_pop_terra_1992(0.05)
