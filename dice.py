import random

würfel_design = {
    "würfel_1": ("┌─────────┐", 
                 "│         │", 
                 "│    ●    │", 
                 "│         │", 
                 "└─────────┘"),
    "würfel_2": ("┌─────────┐", 
                 "│  ●      │", 
                 "│         │", 
                 "│      ●  │", 
                 "└─────────┘"),
    "würfel_3": ("┌─────────┐", 
                 "│  ●      │", 
                 "│    ●    │", 
                 "│      ●  │", 
                 "└─────────┘"),
    "würfel_4": ("┌─────────┐", 
                 "│  ●   ●  │", 
                 "│         │", 
                 "│  ●   ●  │", 
                 "└─────────┘"),
    "würfel_5": ("┌─────────┐", 
                 "│  ●   ●  │", 
                 "│    ●    │", 
                 "│  ●   ●  │", 
                 "└─────────┘"),
    "würfel_6": ("┌─────────┐", 
                 "│  ●   ●  │", 
                 "│  ●   ●  │", 
                 "│  ●   ●  │", 
                 "└─────────┘"),                              
}                                   # Das Design der Würfel 


def start_wuerfel():
    print("Start des Spiels")
    würfel_resultat = [] # Eine leere Liste für die Zwischenresultate
    for würfel in range(5): # Bei Yatzy spielt man jede Runde mit 5 Würfeln, deswegen range 5
        würfeln = random.randint(1, 6) # Es können nur Zahlen zwischen 1 und 6 generiert werden, weil ein Würfel 6 Seiten hat
        würfel_resultat.append(würfeln) # Die Zwischenresultate werden in der Liste gespeichert
    return würfel_resultat 
    
