import pickle 
import menus
import csv
import os

# loaded_user_data = {"anna": "1234", "ben": "geheim"}
# with open('userdata.pkl', 'wb') as userdata:
 #   pickle.dump(loaded_user_data, userdata)

datei = "userdata.csv"
def login():
    if not os.path.exists(datei):
        print("Sie können nicht eingeloggt werden, da noch keine Daten vorhanden sind")
        menus.show_start_menu()

    username = input("Benutzername: ")
    password = input("Passwort: ")

    with open(datei, "r", newline="") as loaded_login_data:
        reader = csv.reader(loaded_login_data)
        for row in reader:
            if row and row[0] == username and row[1] == password: 
                print("Willkommen: ", username)
                menus.show_account_menu()
    print("Benutzername oder Passwort ist falsch!")
    login()



    

