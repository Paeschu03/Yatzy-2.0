import change_userdata
import dice
import end_game
import login
import menues
import tutorial

#-------------------------DEKLARATION METHONEN UND VARIABELN-------------------------#

def test_startausgabe():
    #Wert aus der Startausgabe wird überprüft 
    if user_anweser == "a":
        tutorial_durchführen = input("Möchtest du noch ein kurzes Tutorial durchführen? Ja/Nein")

        if tutorial_durchführen == "Ja":
            tutorial.start_tutorial

        elif user_anweser == "Nein":
            dice.start_wuerfel()

        else:
            print(tutorial_durchführen)
     

    elif user_anweser == "b":
        change_userdata.account_erstellen()

    elif user_anweser == "c":
            login.einloggen()



#-------------------------START DES PROGRAMMES-------------------------#

#Start der ersten Ausgabe
user_anweser = menues.startausgabe() #gibt die Antwort der Startausgabe zurück
test_startausgabe(user_anweser) #Überprüft die Antwort des Benutzer und leitet entsprechend weiter
print("JETZT BIST DU AM ENDE")


