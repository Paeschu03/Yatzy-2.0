from statistics import mean
import menus
import csv
#-------------------------DIE GAMESTATISTIK BEI EINGELOGGTEN SPIELERN WIRD ANGEZEIGT-------------------------#


#with open('stats.csv', 'r') as file: # Hier speichern wir die Daten, um sie später aufrufen zu können
    #pickle.dump(player_stats, file)

def calculate_stats(username):
    '''Erstellt von Anna'''
    scores_for_stats = []
    with open('stats.csv', 'r', newline='', encoding='utf-8') as file: 
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                scores_for_stats.append(int(row['points']))
            else:
                print('Du hast noch kein Spiel gespielt.')


        

            highest_score = max(scores_for_stats)
            lowest_score = min(scores_for_stats)
            average_score = mean(scores_for_stats)
            played_rounds = len(scores_for_stats)

            print(f"Deine Statistik sieht so aus:")
            print(f"- Gespielte Runden: {played_rounds}")
            print(f"- Höchste Punktzahl: {highest_score} Punkte")
            print(f"- Niedrigste Punktzahl: {lowest_score} Punkte")
            print(f"- Durchschnitt: {average_score:.0f} Punkte")
            input("\n[Enter drücken, wenn du parat bist um zurück zum Menu zu kommen]")
            menus.show_account_menu()


