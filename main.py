import change_userdata
import dice
import end_game
import login
import menues
import tutorial
import game
import pickle
from x_abbrechen import eingabe 
import game_stats

#-------------------------DEKLARATION METHONEN UND VARIABELN-------------------------#

def check_anwser_startausgabe(user_anwser):
    #Wert aus der Startausgabe wird überprüft 
    if user_answer == "a":
        tutorial_durchführen = eingabe("Möchtest du noch ein kurzes Tutorial durchführen? Ja/Nein: ")
        if tutorial_durchführen is None:
            return

        if tutorial_durchführen == "Ja":
            tutorial.start_tutorial()

        elif tutorial_durchführen == "Nein": # Müsste das nicht elif tutorial_durchführen sein? oder stimmt elif user_answer?
            game.start_game()

        else:
            print(tutorial_durchführen)
     
    elif user_answer == "b":
        change_userdata.account_erstellen()

    elif user_answer == "c":
        login.einloggen()

        menues.eingeloggte_ausgabe(name)


#-------------------------START DES PROGRAMMES-------------------------#

#Willkommensausgabe
while True:
    user_answer = menues.startausgabe() #gibt die Antwort der Startausgabe zurück
    check_anwser_startausgabe(user_answer) #Überprüft die Antwort des Benutzer und leitet entsprechend weiter


print("JETZT BIST DU AM ENDE")
clear

