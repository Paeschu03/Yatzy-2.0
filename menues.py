import dice 
import login
import tutorial
import change_userdata
import game_stats
import game

from x_abbrechen import eingabe
#-------------------------DIE STARTAUSGABE WIRD AUSGEFÜHRT-------------------------#
def startausgabe():
    print("🎲 🎲 🎲 🎲 🎲 Y-A-T-Z-Y 🎲 🎲 🎲 🎲 🎲")
    print("\nWillkommen bei unserem Yatzy Würfelspiel!")
    print("\nEs gibt noch zwei kleine Sachen zu erklären bevor es losgehen kann.")
    print("1. Du bedienst das Spiel nur mit Buchstaben, die Zahlen gehören zum Gameplay.")
    print("2. Du kannst bei jeder Eingabe mit x und anschliessend Enter zurück zur Startausgabe, falls du's dir anders überlegst.")
    input("\n[Enter drücken, wenn du parat bist um weiter zu machen]")
    print("\nDu kannst zwischen den folgenden Optionen auswählen:")
    print("(A) als Gast spielen")
    print("(B) Account erstellen")
    print("(C) Einloggen")
    print("(D) Spiel schliessen")
    
    aktion = input("Welche Option möchtest du wählen A, B, C oder D? ").lower().strip()

    return aktion


#-------------------------DAS ACCOUNTMENUE WIRD ANGEZEIGT UND AUSGEFÜHRT-------------------------#
def menue_mit_account():
    print("Dir stehen die folgenden Möglichkeiten offen:")
    print("(A) Statistik anzeigen")
    print("(B) Benutzername und Passwort ändern")
    print("(C) Runde spielen")
    print("(D) Tutorial")
    print("(E) Account löschen")
    print("(F) Spiel beenden")
    anwort_menue_mit_account = eingabe("Was möchtest du machen? A, B, C, D, E oder F? ")
    if anwort_menue_mit_account is None:
        return
    anwort_menue_mit_account = anwort_menue_mit_account.strip().lower()
    if anwort_menue_mit_account == "a":
        game_stats.game_stats()
    elif anwort_menue_mit_account == "b":
        change_userdata.change_username_and_password()
    elif anwort_menue_mit_account == "c":
        game.start_game()
    elif anwort_menue_mit_account == "d":
        tutorial.start_tutorial()
    elif anwort_menue_mit_account == "e":
        change_userdata.delete_user()
    elif anwort_menue_mit_account == "f":
            exit()
    else:
        print("Diese Auswahl ist ungültig!")
        menue_mit_account()

        


    

