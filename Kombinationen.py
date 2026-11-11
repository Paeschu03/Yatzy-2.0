from x_abbrechen import eingabe
import game

KATEGORIEN = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer","Sechser", "Ein Paar", "Zwei Paare","Drilling","Vierling","Kleine Strasse", "Grosse Strasse", "Full House","Chance", "Yatzy"]

BUCHSTABEN = ["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]

spielzettel = {}

def neuer_spielzettel():
    
    for kategorie in KATEGORIEN:
        spielzettel[kategorie] = None
    return spielzettel

def uebersicht_anzeigen(spielzettel):
    print("Übersicht der Kombinationen:")
    for index in range(len(KATEGORIEN)):
        kategorie = KATEGORIEN[index]
        buchstabe = BUCHSTABEN[index]

        if spielzettel[kategorie] is None:
            print(buchstabe, "-", kategorie, "- offen")
        else:
            print(buchstabe, "-", kategorie, "- belegt")

def kategorie_eintragen(spielzettel, wuerfel, auswahl):
    for index in range(len(BUCHSTABEN)):
        if auswahl == BUCHSTABEN[index]:
            kategorie = KATEGORIEN[index]
            if spielzettel[kategorie] is not None:
                print("Diese Kombination ist bereits belegt.")
                return False
            # Eine Kopie der Würfelwerte für diese Kategorie speichern.
            spielzettel[kategorie] = list(wuerfel)
            print("Du hast", kategorie, "ausgewählt.")
            uebersicht_anzeigen(spielzettel)
            game.start_game()
            return True
    print("Bitte einen Buchstaben von a bis o eingeben.")
    return False

def auswahl_nach_wurf(spielzettel, wuerfel, wurfnummer):
    print("Wurf", wurfnummer, "von 3")
    print("Deine Würfel:", wuerfel)
    uebersicht_anzeigen(spielzettel)
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
            erfolgreich = kategorie_eintragen(
                spielzettel, wuerfel, auswahl )
            if erfolgreich:
                return "eingetragen"