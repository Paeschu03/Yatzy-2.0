from input_handling import eingabe
#import game

CATEGORIES = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer","Sechser", "Ein Paar", "Zwei Paare","Drilling","Vierling","Kleine Strasse", "Grosse Strasse", "Full House","Chance", "Yatzy"]

LETTERS = ["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o"



def create_scorecard():
    scorecard = {}
    for category in CATEGORIES:
        scorecard[category] = None

    return scorecard

def display_scorecard(spielzettel):
    print("Übersicht der Kombinationen:")
    for index in range(len(KATEGORIEN)):
        kategorie = KATEGORIEN[index]
        buchstabe = BUCHSTABEN[index]

        if spielzettel[kategorie] is None:
            print(buchstabe, "-", kategorie, "- offen")
        else:
            print(buchstabe, "-", kategorie, "- belegt")

def record_category(spielzettel, wuerfel, auswahl):
    for index in range(len(BUCHSTABEN)):
        if auswahl == BUCHSTABEN[index]:
            kategorie = KATEGORIEN[index]
            if spielzettel[kategorie] is not None:
                print("Diese Kombination ist bereits belegt.")
                return False
            # Eine Kopie der Würfelwerte für diese Kategorie speichern.
            spielzettel[kategorie] = list(wuerfel)
            print("Du hast", kategorie, "ausgewählt.")
            display_scorecard(spielzettel)
            #game.start_game()
            return True
    print("Bitte einen Buchstaben von a bis o eingeben.")
    return False

def select_category_after_roll(spielzettel, wuerfel, wurfnummer):
    print("Wurf", wurfnummer, "von 3")
    print("Deine Würfel:", wuerfel)
    display_scorecard(spielzettel)
    while True:
        if wurfnummer < 3:
            print("W = weiterwürfeln")
        else:
            print("Dritter Wurf: Wähle eine offene Kombination.")
        auswahl = eingabe( "Kombination a bis o wählen (X = Startausgabe): "  )
        if auswahl is None:
            return None
        auswahl = auswahl.strip().lower()
        if auswahl == "w":
            if wurfnummer < 3:
                return "weiter"
            print("Nach dem dritten Wurf kannst du nicht weiterwürfeln.")
        else:
            erfolgreich = record_category(
                spielzettel, wuerfel, auswahl )
            if erfolgreich:
                return "eingetragen"