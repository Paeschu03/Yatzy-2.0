import dice 
import login
import tutorial
import change_userdata
import game_stats
import main

from x_abbrechen import eingabe

def startausgabe():
    print("Willkommen bei unserem Spiel Yatzy!")
    print("\n Test")
    aktion = input("(A) als Gast spielen, (B) Account erstellen oder (C) Einloggen: ").lower().strip()

    return aktion

def menue_mit_account():
    print("Dir stehen die folgenden Möglichkeiten offen:")
    print("A) Statistik anzeigen")
    print("B) Benutzername und Passwort ändern")
    print("C) Runde spielen")
    print("D) Tutorial")
    print("E) Account löschen")
    anwort_menue_mit_account = eingabe("Was möchtest du machen? A, B, C, D, oder E")
    if anwort_menue_mit_account is None:
        return
    anwort_menue_mit_account = anwort_menue_mit_account.strip().lower()
    if anwort_menue_mit_account == "a":
        game_stats()
    elif anwort_menue_mit_account == "b":
        change_userdata.change_username_and_password()
    elif anwort_menue_mit_account == "c":


    

