import user_management
import dice
import end_game
import login
import menus
import tutorial
import game
import pickle
from input_handling import get_input
import game_stats


#------------------------------------------------------------------------------------#
#-------------------------DEKLARATION METHONEN UND VARIABELN-------------------------#
#------------------------------------------------------------------------------------#
def check_start_menu_answer(user_answer):
    if user_answer == "a":
        tutorial_choice = get_input("Möchtest du noch ein kurzes Tutorial durchführen? Ja/Nein: ")
        if tutorial_choice is None:
            return

        tutorial_choice = tutorial_choice.strip().lower()
        if tutorial_choice == "ja":
            tutorial.start_tutorial()

        elif tutorial_choice == "nein": 
            game.start_game()

                
    elif user_answer == "b":
        change_userdata.create_account()

    elif user_answer == "c":
        login.login()

    elif user_answer == "d":
        exit()

    elif user_answer != 'a' or user_answer != 'b' or user_answer != 'c' or user_answer != 'd':
        print("Eingabe trifft auch keine Menüoption")
        user_answer = menues.startausgabe()
        check_answer_startausgabe(user_answer)
    

        #menues.eingeloggte_ausgabe(name)


#------------------------------------------------------------------------------------#
#--------------------------------START DES PROGRAMMS---------------------------------#
#------------------------------------------------------------------------------------#

#Willkommensausgabe
#while True:
menues.programmerklärung()
user_answer = menues.startausgabe() #gibt die Antwort der Startausgabe zurück
check_answer_startausgabe(user_answer) #Überprüft die Antwort des Benutzer und leitet entsprechend weiter




