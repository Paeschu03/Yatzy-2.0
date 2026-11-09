WUERFEL = {1: ("┌─────────┐", 
                 "│         │", 
                 "│    ●    │", 
                 "│         │", 
                 "└─────────┘"), 
             2: ("┌─────────┐", 
                 "│  ●      │", 
                 "│         │", 
                 "│      ●  │", 
                 "└─────────┘"), 
             3: ("┌─────────┐", 
                 "│  ●      │", 
                 "│    ●    │", 
                 "│      ●  │", 
                 "└─────────┘"), 
             4: ("┌─────────┐", 
                 "│  ●   ●  │", 
                 "│         │", 
                 "│  ●   ●  │", 
                 "└─────────┘"), 
             5: ("┌─────────┐", 
                 "│  ●   ●  │", 
                 "│    ●    │", 
                 "│  ●   ●  │", 
                 "└─────────┘"), 
             6: ("┌─────────┐", 
                 "│  ●   ●  │", 
                 "│  ●   ●  │", 
                 "│  ●   ●  │", 
                 "└─────────┘")}


def weiter():
    input("\n[Enter drücken, wenn du parat bist um weiter zu machen]")

def zeige_wuerfel(wuerfe):
    for zeile in range(5):
        teile = []
        for w in wuerfe:
            teile.append(WUERFEL[w][zeile])
        print("  ".join(teile))

def start_tutorial():
    
    print("\nWillkommen bei Tutorial!")
    
    print("\nZiel: Möglichst viele Punkte mit 5 Würfeln sammeln.")
    print("\nDas Spiel hat 15 Runden, in jeder Runde füllst du eine Kategorie.")
    print("\nPro Runde kannst du deine 5 Würfel maximal 3x Würfeln")
    weiter()

    
    print("\n1. Mal Würfeln")
    
    print("Pro Runde darfst du bis zu 3-mal würfeln.")
    print("Nach jedem Wurf kannst du Würfel behalten und den Rest neu werfen.")
    print("\nBeispiel – erster Wurf:")
    print("\nBeispiel – erster Wurf:")
    zeige_wuerfel([3, 3, 5, 1, 3])
    print("\nDu behältst die drei 3er und würfelst die anderen zwei neu:")
    zeige_wuerfel([3, 3, 3, 3, 6])
    weiter()

    
    print("\n2. Oberer Teil")
    
    
    print("Einer bis Sechser: Du zählst nur die Würfel mit dieser Zahl.")
    print("Beispiel: [3, 3, 3, 3, 6] bei 'Dreier' = 12 Punkte")
    print("Bonus: Ab 63 Punkten im oberen Teil gibt es 50 Extrapunkte.")
    weiter()

    
    print("\n3. Oberer Teil")
    
    print("Ein Paar, Zwei Paare, Drilling, Vierling")
    print("Kleine Strasse (1-5) = 15, Grosse Strasse (2-6) = 20")
    print("Full House (3 + 2 gleiche) = Summe aller Würfel")
    print("Chance = Summe aller Würfel, egal welche")
    print("Yatzy (5 gleiche) = 50 Punkte")
    weiter()

    
    print("\nKurzer Test")
    
    zeige_wuerfel([2, 2, 5, 5, 5])
    antwort = input("Wie viele Punkte gibt das als Full House? ")
    if antwort.strip() == "19":
        print("Richtig! 2+2+5+5+5 = 19")
    else:
        print("Nicht ganz – Full House ist die Summe: 2+2+5+5+5 = 19")

    return


    


