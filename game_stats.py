import pickle
from statistics import mean
import menues

#-------------------------DIE GAMESTATISTIK BEI EINGELOGGTEN SPIELERN WIRD ANGEZEIGT-------------------------#

player_stats = {                             # Das sind vorgespeicherte Daten, damit wir bei der Präsentation die Statistik zeigen können
    "pia": [611, 530, 326, 403, 540, 489],
    "anna": [503, 621, 303, 487, 522, 380],
    "pascal": [550, 498, 320, 603, 500],
    "dilara": [500, 340, 476, 607, 401],
    "selina" : []
}


with open('player_stats.pkl', 'wb') as file: # Hier speichern wir die Daten, um sie später aufrufen zu können
    pickle.dump(player_stats, file)

def game_stats(player_stats):
    '''Erstellt von Anna'''
    with open('player_stats.pkl', 'rb') as file: # Hier werden die gespeicherten Daten aufgerufen
        player_stats = pickle.load(file)


        for player, scores in player_stats.items(): # Statistiken pro Spieler werden berechnet
            if not scores:  # Falls keine Runden gespielt wurden
                print("Du hast noch keine Runden gespielt.")
                continue

            highest_score = max(scores)
            lowest_score = min(scores)
            average_score = mean(scores)
            played_rounds = len(scores)

            print(f"Deine Statistik sieht so aus:")
            print(f"- Gespielte Runden: {played_rounds}")
            print(f"- Höchste Punktzahl: {highest_score} Punkte")
            print(f"- Niedrigste Punktzahl: {lowest_score} Punkte")
            print(f"- Durchschnitt: {average_score:.0f} Punkte")
            input("\n[Enter drücken, wenn du parat bist um zurück zum Menu zu kommen]")
            menues.menue_mit_account()

# Diese Game Statistik arbeitet erst mit den Beispielwerten von player_stats. Ich bin mir noch sehr unsicher, wie wir die tatsächlichen Werte 
# einspeisen können
