from input_handling import get_input
import pickle 
import menus
import csv
import os

#loaded_user_data = {"anna": "1234", "ben": "geheim"}
#with open('userdata.pkl', 'wb') as userdata:
#    pickle.dump(loaded_user_data, userdata)



datei = "userdata.csv"

def create_account():
    if not os.path.exists(datei):
        with open(datei, "w", newline="") as login_data:
            writer = csv.writer(login_data)
            writer.writerow(["username", "password"])


    username = input("Benutzername: ")
    password = input("Passwort: ")

    with open(datei, "r", newline="") as login_data:
        reader = csv.reader(login_data)
        for row in reader: 
            if row and row[0] == username:
                print("Diesen Benutzernamen gibt es schon")
                create_account()
            
        with open(datei, "a", newline="") as login_data:
            writer = csv.writer(login_data)
            writer.writerow([username, password])
            print("Der Benutzer wurde erfolgreich angelegt")     


def change_username_and_password():
    if not os.path.exists(datei):
        with open(datei, "w", newline="") as login_data:
            writer = csv.writer(login_data)
            writer.writerow(["username", "password"])

    username = input("Benutzername: ")
    password = input("Passwort: ")

    with open(datei, "r", newline="") as loaded_data:
        reader = csv.reader(loaded_data)
        all_data = list(reader)

    # 1. Nur suchen und merken
    user_row = None
    for row in all_data:
        if row and row[0] == username and row[1] == password:
            user_row = row

    # 2. Erst nach der Schleife entscheiden
    if user_row is None:
        print("Benutzername oder Passwort falsch!")
        change_username_and_password()
        

    anwser = input("Wollen Sie (A) Benutzernamen oder (B) Passwort ändern? ")

    if anwser == "A" or anwser == "a":
        new_unsername = input("Neuer Benutzername: ")
        for other_row in all_data:
            if other_row and other_row[0] == new_unsername:
                print("Benutzernamen schon vergeben")
                change_username_and_password()
                
        user_row[0] = new_unsername
        print("Benutzername wurde geändert.")
        with open(datei, "w", newline="") as login_data:
                writer = csv.writer(login_data)
                writer.writerows(all_data)
        menus.show_account_menu()

    elif anwser == "B" or anwser == "b":
        new_password = input("Neues Passwort: ")
        user_row[1] = new_password
        print("Passwort wurde geändert.")
        with open(datei, "w", newline="") as login_data:
                writer = csv.writer(login_data)
                writer.writerows(all_data)
        menus.show_account_menu()

    else:
        print("Ungültige Auswahl.")
        #weiterleitung noch reinnehmen


def delete_user():
    if not os.path.exists(datei):
        print("Es gibt noch keine Benutzer.")
        return

    username = input("Benutzername: ")
    password = input("Passwort: ")

    with open(datei, "r", newline="") as loaded_data:
        reader = csv.reader(loaded_data)
        all_data = list(reader)

    # 1. Nur suchen und merken
    user_row = None
    for row in all_data:
        if row and row[0] == username and row[1] == password:
            user_row = row

    # 2. Erst nach der Schleife entscheiden
    if user_row is None:
        print("Benutzername oder Passwort falsch!")
        return

    anwser = input("Willst du deinen Account wirklich löschen? (J/N) ")
    if anwser != "J" and anwser != "j":
        print("Löschen abgebrochen.")
        return

    # 3. Zeile aus der Liste entfernen
    all_data.remove(user_row)

    # 4. Liste zurück in die Datei schreiben
    with open(datei, "w", newline="") as login_data:
        writer = csv.writer(login_data)
        writer.writerows(all_data)

    print("Der Account " + username + " wurde gelöscht.")
        