def punkte_berechnen(kategorie, wuerfel):
    zahlen = ( "Einser": 1, "Zweier": 2, "Dreier": 3, "Vierer": 4, "Fünfer": 5, "Sechser": 6 )

    if kategorie in zahlen:
        zahl = zahlen[kategorie]
        return wuerfel.count(zahl) * zahl

    elif kategorie == "Ein Paar":
        punkte = 0
        for zahl in range(1, 7):
            if wuerfel.count(zahl) >= 2:
                punkte = zahl * 2
        return punkte
    
    elif kategorie == "Zwei Paare":
        paare = []
        for zahl in range(1, 7):
            if wuerfel.count(zahl) >= 2:
                paare.append(zahl)
        if len(paare) == 2:
            return sum(paare) * 2
        
        return 0
    
    elif kategorie == "Drilling":
        for zahl in range(1, 7):
            if wuerfel.count(zahl) >= 3:
                return zahl * 3
            
        return 0

    elif kategorie == "Vierling":
        for zahl in range(1, 7):
            if wuerfel.count(zahl) >= 4:
                return zahl * 4
        return 0

    elif kategorie == "Kleine Strasse":
        if sorted(wuerfel) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    elif kategorie == "Grosse Strasse":
        if sorted(wuerfel) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    elif kategorie == "Full House":
        paar = False
        drilling = False

        for zahl in range(1, 7):
            if wuerfel.count(zahl) == 2:
                paar = True

            if wuerfel.count(zahl) == 3:
                drilling = True

        if paar and drilling:
            return sum(wuerfel)

        return 0

    elif kategorie == "Chance":
        return sum(wuerfel)

    elif kategorie == "Yatzy":
        if wuerfel.count(wuerfel[0]) == 5:
            return 50

        return 0

    return 0
