import dice 
import login
import tutorial
import change_userdata

from x_abbrechen import eingabe

def startausgabe():
    print("Willkommen bei unserem Spiel Yatzy!")
    print("\n Test")
    aktion = input("(A) als Gast spielen, (B) Account erstellen oder (C) Einloggen: ").lower().strip()

    return aktion

