
def pythagoras(cateta1, cateta2, ipotenuza):
        if cateta1 == str("x"):
            return ("Cateta 1 = " + str(((ipotenuza**2) - (cateta2**2))/2))
        elif cateta2 == str("x"):
            return ("Cateta 2 = " + str(((ipotenuza**2) - (cateta1**2))/2))
        elif ipotenuz == str("x"):
            return ("Ipotenuza = " + str(((cateta1**2) + (cateta2**2))/2))
        else:
            return "Se stiu toate laturile."
