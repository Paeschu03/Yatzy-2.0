import dice 
import login
import tutorial
import change_userdata

def startausgabe():
    print("Herzlich willkommen zu unserem Yatzy, wie möchtest du vorgehen? ")
    aktion = input("(A) als Gast spielen, (B) Account erstellen oder (C) Einloggen: ").lower().strip()

    if aktion == "a":
        tutorial_durchführen = input("Möchtest du noch ein kurzes Tutorial durchführen? Ja/Nein")

        if tutorial_durchführen == "Ja":
            tutorial.start_tutorial

        elif aktion == "Nein":
            dice.start_wuerfel()

        else:
            print(tutorial_durchführen)

        

    elif aktion == "b":
        change_userdata.account_erstellen()

    elif aktion == "c":
        login.einloggen()