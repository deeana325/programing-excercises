#   în fiecare zi lucrătoare din săptămână, Pinocchio spune o minciună în urma
# căreia îi creste nasul cu x cm pe zi.  Sâmbăta şi duminica, când vine Gepetto acasă,
# pentru a nu-l supăra, nu spune nici o minciună, ba chiar îi scade nasul cu y cm / zi.
# În fiecare săptămână, singur acasă, Pinocchio continua şirul minciunilor.  Care este
# lungimea nasului dupa z zile, ştiind că inițial nasul are p cm?  (Zilele încep cu luni)
# d = ziua saptamanii (1->5 zile lucratoare, 6->7 sambata si duminica)


def lungime(z: int, p: float, x: float, y: float, d:int = 1) -> float:
    if z == 0:
        return p
    elif z in [6, 7]:
        if z == 7:
            lungime(z - 1, p + y, x, y, d = 1)
        else:
            lungime(z - 1, p + y, x, y, d + 1)
    else:
        lungime(z - 1, p + x, x, y, d + 1)


def cat_de_mare_e_nasul_lui_pinochio(z: int, p: float, x: float, y: float):
    print("Lungimea nasului lui pinochio dupa", z, "zile este", lungime(z, p, x, y), "cm.")


assert cat_de_mare_e_nasul_lui_pinochio(5, 0, 1, 0) == 5, "Wrong answer"


cat_de_mare_e_nasul_lui_pinochio(25, 2.6, 1.75, 0.3)
