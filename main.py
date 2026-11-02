import change_userdata
import dice
import end_game
import login
import menues
import tutorial
import game

#-------------------------DEKLARATION METHONEN UND VARIABELN-------------------------#

def check_anwser_startausgabe(user_anwser):
    #Wert aus der Startausgabe wird überprüft 
    if user_answer == "a":
        tutorial_durchführen = input("Möchtest du noch ein kurzes Tutorial durchführen? Ja/Nein: ")

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



#-------------------------START DES PROGRAMMES-------------------------#

#Willkommensausgabe
user_answer = menues.startausgabe() #gibt die Antwort der Startausgabe zurück
check_anwser_startausgabe(user_answer) #Überprüft die Antwort des Benutzer und leitet entsprechend weiter


print("JETZT BIST DU AM ENDE")


