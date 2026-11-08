import dice 
import login
import tutorial
import change_userdata

from hilfsfunktionen import eingabe

def startausgabe():
    print("Willkommen bei unserem Spiel Yatzy!")
    print("\n Test")
    aktion = input("(A) als Gast spielen, (B) Account erstellen oder (C) Einloggen: ").lower().strip()

    return aktion

#def startausgabe():
   # print()
   # print("Willkommen bei unserem Spiel Yatzy!")
   # print("A = Als Gast spielen")
   # print("B = Account erstellen")
   # print("C = Einloggen")

  #  aktion = eingabe("Deine Auswahl: ")

  #  if aktion is None:
  #       return None
  # aktion = aktion.strip()
  # aktion = aktion.lower()
  # return aktion

#def eingeloggte_ausgabe(name):
   # print()
   # print("Willkommen,", name)
   # print("Du bist eingeloggt.")

   # while True:
       # antwort = eingabe(
       #  "X = abmelden und zur Startausgabe zurückkehren: " )

      #  if antwort is None:
     #       return

     #   print("Bitte X eingeben, um dich abzumelden.")

