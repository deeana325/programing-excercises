#   Izotopul radioactiv de plutoniu 135 are perioada de înjumătățire de 26 minute,
# adică după 26 minute doar jumătate din izotop va mai rămâne.  După alte 26 minute doar
# jumătate din această jumătate ş.a.m.d.  Scrieți un program care va determina cât timp
# îi va lua plutoniului 135 să scadă până la punctul în care un procent specificat din
# cantitatea inițială a mai rămas.
#   Exemplu.  Pentru un procent dat de 0.58 timpul necesar este de 208 min.


def cat_timp(procent_dorit: float, timp: int = 0, procent_izotop: float = 100) -> int:
    if procent_izotop <= procent_dorit:
        return timp
    else:
        cat_timp(procent_dorit, timp + 26, procent_izotop / 2)
        

def cat_ii_ia_izotopului_plutoniu_135_sa_ajunga_la_procentul_dorit(procent_dorit: float):
    print("Izotopului radioactiv de plutoniu 135 ii ia", cat_timp(procent_dorit), "minute sa ajunga la", procent_dorit,
    "%\ din cantitatea initiala.")


assert cat_timp(0.58) == 208, "Wrong answer" 


cat_ii_ia_izotopului_plutoniu_135_sa_ajunga_la_procentul_dorit(0.58)  
