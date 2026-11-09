from statistics import mean
from hilfsfunktionen import eingabe

def game_stats(*scores): # Das Sternchen vor "scores" bedeutet dass kein Limit an Werten bestimmt wurde, was hier benötigt wird weil sich die Werte ständig verändern
    durchschnitt_aller_runden = mean(scores) # Mean ist im Deutschen der Durchschnitt
    höchste_punktzahl = max(scores)
    niedrigste_punktzahl = min(scores)
    zahl_der_durchgänge = len(scores)
    print(f"Du hast bereits {zahl_der_durchgänge} Runden gespielt.")
    print(f"Dein Highlight lag bei {höchste_punktzahl} Punkten, gratuliere!")
    print(f"Der niedrigste Wert deiner Runden ist {niedrigste_punktzahl} Punkte, schade!")
    print(f"Der Durchschnitt deiner Runden beträgt {durchschnitt_aller_runden:.0f} Punkte.")

    # Wie soll ich hier die hilfsfunktion implementieren?
    # Scores ist ein Platzhalter der je nach Dilaras Variabelnamen geändert werden muss
    