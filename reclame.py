from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    kortingbedrag = prijs * korting
    nieuwe_prijs = prijs - korting

    aanbieding = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro"

    return aanbieding

smaak = "aardbei"
prijs = 4
korting = 0.1

resultaat = aanbieding_1(smaak, prijs, korting)

print(resultaat)

def inkomsten_totaal(inkomsten,btw):
    inkomsten_week = sum(inkomsten)
    btw_week = inkomsten_week * 0.09

    totaal = f"Het totaal van alle inkomsten deze week is {inkomsten_week} euro, waarover {btw_week} euro btw betaalt dient te worden."

    return totaal

inkomsten_dag = [220, 430, 125, 160, 205, 90, 345]
inkomsten = 345
btw = 0.09

daginkomsten = inkomsten_totaal(inkomsten_dag, btw)

print(daginkomsten)

def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    return laag, hoog

resultaten = laag_en_hoog(inkomsten_dag)

print(resultaten)

def gemiddelde (mijn_lijst):
    gemiddelde_omzet = sum(mijn_lijst) / len(mijn_lijst)
    gemiddeld_week = f"De gemiddelde inkomsten deze week zijn {gemiddelde_omzet} euro."

    return gemiddeld_week

bereken_gemiddelde = gemiddelde(inkomsten_dag)

print(bereken_gemiddelde)

def meervoudig(invoer_lijst):
    nieuwe_hoog_laag = laag_en_hoog(invoer_lijst)
    return nieuwe_hoog_laag

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]

resultaat_meervoudig = meervoudig(invoer_lijst)

print(resultaat_meervoudig)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

print(combinatie)