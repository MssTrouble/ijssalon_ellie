from helper import decoreer

def print_aanbieding():      
    prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }

    aanbieding = 0.8 * (prijzen["aardbei"])
    reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts €{aanbieding}"
    reclame_tekst2 = reclame_tekst[:62]
    reclame_tekst3 = (reclame_tekst2).upper()
    reclame_tekst4 = (reclame_tekst3).split()

    el = (reclame_tekst4)
    for i in el:
        if len(i) >= 5:
            print(i.upper())
        else:
            print(i.lower())

decoreer("Aanbieding")
print_aanbieding()