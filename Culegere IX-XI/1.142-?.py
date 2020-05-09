#   In povestea "Jack şi vrejul de fasole", Jack trebuia să ajungă în Tara Uriaşului,
# situată la x metrii deasupra pământului, urcând cu vrejul de fasole care avea proprietatea
# miraculoasă de a creşte în fiecare minut cu 1/2, 1/3, 1/4, etc. din înălțimea lui anterioară
# (înălțimea inițială a vrejului este 1 m).
#   În câte minute ajunge Jack în Tara Uriaşului?
#   Exemplu.  Dacă x = 300 Jack a boy in the dupa 598 de minute.


def timp_pana_in_tara_uriasului(lungimea_vrejului: float, timp:int, x:float) -> int:
    if lungimea_vrejului >= x:
        return timp
    else:
        timp_pana_in_tara_uriasului(lungimea_vrejului + lungimea_vrejului / (timp + 2), timp + 1, x)


def cat_ii_ia_lui_jack_sa_urce(distanta_pana_in_tara_uriasului:float):
    print("Jack ajunge in varf dupa", timp_pana_in_tara_uriasului(1, 0, distanta_pana_in_tara_uriasului), "de minute")
    

assert timp_pana_in_tara_uriasului(1, 0, 300) == 598, "Wrong result"


cat_ii_ia_lui_jack_sa_urce(300)
