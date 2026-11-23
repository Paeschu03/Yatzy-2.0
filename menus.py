import dice 
import login
import tutorial
import change_userdata
import game_stats
import game

from input_handling import get_input
#-------------------------DIE STARTAUSGABE WIRD AUSGEFÜHRT-------------------------#
def show_start_menu():
    print("🎲 🎲 🎲 🎲 🎲 Y-A-T-Z-Y 🎲 🎲 🎲 🎲 🎲")
    print("\nWillkommen bei unserem Yatzy Würfelspiel!")
    print("\nEs gibt noch zwei kleine Sachen zu erklären bevor es losgehen kann.")
    print("1. Du bedienst das Spiel nur mit Buchstaben, die Zahlen gehören zum Gameplay.")
    print("2. Du kannst bei jeder Eingabe mit x und anschliessend Enter zurück zur Startausgabe, falls du's dir anders überlegst.")
    input("\n[Enter drücken, wenn du parat bist um weiter zu machen]")
    return

def show_start_menu():
    print("\033[H\033[2J\033[3J", end="")
    print("\nDu kannst zwischen den folgenden Optionen auswählen:")
    print("(A) als Gast spielen")
    print("(B) Account erstellen")
    print("(C) Einloggen")
    print("(D) Spiel schliessen")
    
    action = input("Welche Option möchtest du wählen A, B, C oder D? ").lower().strip()

    return action


#-------------------------DAS ACCOUNTMENUE WIRD ANGEZEIGT UND AUSGEFÜHRT-------------------------#
def show_account_menu():
    '''Erstellt von Anna'''
    print("\nDir stehen die folgenden Möglichkeiten offen:")
    print("(A) Statistik anzeigen")
    print("(B) Benutzername und Passwort ändern")
    print("(C) Runde spielen")
    print("(D) Tutorial")
    print("(E) Account löschen")
    print("(F) Spiel beenden")
    account_menu_answer = get_input("Was möchtest du machen? A, B, C, D, E oder F? ")
    if account_menu_answer is None:
        return
    account_menu_answer = account_menu_answer.strip().lower()
    if account_menu_answer == "a":
        game_stats.game_stats()
    elif account_menu_answer == "b":
        change_userdata.change_username_and_password()
    elif account_menu_answer == "c":
        game.start_game()
    elif account_menu_answer == "d":
        tutorial.start_tutorial()
    elif account_menu_answer == "e":
        change_userdata.delete_user()
    elif account_menu_answer == "f":
            exit()
    else:
        print("Diese Auswahl ist ungültig!")
        show_account_menu()

        


    

