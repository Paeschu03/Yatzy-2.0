from input_handling import get_input
from scoring import calculate_points
#import game

CATEGORIES = ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer","Sechser", "Ein Paar", "Zwei Paare","Drilling","Vierling","Kleine Strasse", "Grosse Strasse", "Full House","Chance", "Yatzy"]

LETTERS = ["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]



def create_scorecard():
    scorecard = {}
    for category in CATEGORIES:
        scorecard[category] = None

    return scorecard

def show_scorecard(scorecard):
    print("Übersicht der Kombinationen:")
    for index in range(len(CATEGORIES)):
        category = CATEGORIES[index]
        letter = LETTERS[index]
        if scorecard[category] is None:
            print(letter, "-", category, "- offen")
        else:
            print(letter, "-", category, "-", scorecard[category], "Punkte")
#Gesamtpunktzahl berechnen
    total_points = 0
    for category in CATEGORIES:
        if scorecard[category] is not None:
            total_points += scorecard[category]
    print("Gesamtpunktzahl:", total_points, "Punkte")


def record_category(scorecard, dice, choice):
    for index in range(len(LETTERS)):
        if choice == LETTERS[index]:
            category = CATEGORIES[index]
            if scorecard[category] is not None:
                print("Diese Kombination ist bereits belegt.")
                return False
            # Eine Kopie der Würfelwerte für diese Kategorie speichern.
            scorecard[category] = list(dice)
            print("Du hast", category, "ausgewählt.")
            show_scorecard(scorecard)
            #game.start_game()
            return True
    print("Bitte einen Buchstaben von a bis o eingeben.")
    return False

def select_category_after_roll(scorecard, dice, throw_number):
    print("Wurf", throw_number, "von 3")
    print("Deine Würfel:", dice)
    show_scorecard(scorecard)
    while True:
        if throw_number < 3:
            print("W = weiterwürfeln")
        else:
            print("Dritter Wurf: Wähle eine offene Kombination.")
        choice = get_input( "Kombination a bis o wählen (X = Startausgabe): "  )
        if choice is None:
            return None
        choice = choice.strip().lower()
        if choice == "w":
            if throw_number < 3:
                return "weiter"
            print("Nach dem dritten Wurf kannst du nicht weiterwürfeln.")
        else:
            successful = record_category(scorecard, dice, choice )
            if successful:
                return "eingetragen"