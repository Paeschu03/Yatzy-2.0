import dice 
import login
import tutorial
import change_userdata

def startausgabe():
    print("Herzlich willkommen zu unserem Yatzy, wie möchtest du vorgehen? ")
    aktion = input("(A) als Gast spielen, (B) Account erstellen oder (C) Einloggen: ").lower().strip()

    return aktion

