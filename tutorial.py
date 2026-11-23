DICE = {1: ("┌─────────┐", 
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


def continue_tutorial():
    input("\n[Enter drücken, wenn du parat bist um weiter zu machen]")

def show_dice(wuerfe):
    for row_number in range(5):
        row_parts = []
        for w in wuerfe:
            row_parts.append(DICE[w][row_number])
        print("  ".join(row_parts))

def start_tutorial():
    
    print("\nWillkommen bei Tutorial!")
    
    print("\nZiel: Möglichst viele Punkte mit 5 Würfeln sammeln.")
    print("\nDas Spiel hat 15 Runden, in jeder Runde füllst du eine Kategorie.")
    print("\nPro Runde kannst du deine 5 Würfel maximal 3x Würfeln")
    continue_tutorial()

    
    print("\n1. Mal Würfeln")
    
    print("Pro Runde darfst du bis zu 3-mal würfeln.")
    print("Nach jedem Wurf kannst du Würfel behalten und den Rest neu werfen.")
    print("\nBeispiel – erster Wurf:")
    print("\nBeispiel – erster Wurf:")
    show_dice([3, 3, 5, 1, 3])
    print("\nDu behältst die drei 3er und würfelst die anderen zwei neu:")
    show_dice([3, 3, 3, 3, 6])
    continue_tutorial()

    
    print("\n2. Oberer Teil")
    
    
    print("Einer bis Sechser: Du zählst nur die Würfel mit dieser Zahl.")
    print("Beispiel: [3, 3, 3, 3, 6] bei 'Dreier' = 12 Punkte")
    print("Bonus: Ab 63 Punkten im oberen Teil gibt es 50 Extrapunkte.")
    continue_tutorial()

    
    print("\n3. Oberer Teil")
    
    print("Ein Paar, Zwei Paare, Drilling, Vierling")
    print("Kleine Strasse (1-5) = 15, Grosse Strasse (2-6) = 20")
    print("Full House (3 + 2 gleiche) = Summe aller Würfel")
    print("Chance = Summe aller Würfel, egal welche")
    print("Yatzy (5 gleiche) = 50 Punkte")
    continue_tutorial()

    
    print("\nKurzer Test")
    
    show_dice([2, 2, 5, 5, 5])
    user_answer = input("Wie viele Punkte gibt das als Full House? ")
    if user_answer.strip() == "19":
        print("Richtig! 2+2+5+5+5 = 19")
    else:
        print("Nicht ganz – Full House ist die Summe: 2+2+5+5+5 = 19")

    return


