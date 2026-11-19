from input_handling import eingabe
import pickle 
import menus

#loaded_user_data = {"anna": "1234", "ben": "geheim"}
#with open('userdata.pkl', 'wb') as userdata:
#    pickle.dump(loaded_user_data, userdata)

with open('userdata.pkl', 'rb') as userdata:
   loaded_dict = pickle.load(userdata)


def create_account():
    create_new_user = eingabe("Möchtest du einen neuen Benutzer anlegen? ")
    if create_new_user is None:
        return
    create_new_user = create_new_user.strip().lower()
    if create_new_user in ["ja", "j", "yes", "jo", "klar", "ju"]:
        new_username = eingabe("Oke. Dann gebe nun deinen gewünschten Benutzernamen ein: ")
        if new_username is None:
            return
        new_username = new_username.strip()
        new_password = eingabe("Gebe nun ein Passwort ein: ")
        if new_password is None:
            return
        loaded_dict[new_username] = new_password
        with open('userdata.pkl', 'wb') as datei:   # 'wb' = Datei komplett überschreiben        
            pickle.dump(loaded_dict, datei)
        print(f"Dein Benutzerkonto mit dem Benutzernamen {new_username} und dem Passwort {new_password} wurden nun angelegt.")
        menus.menue_mit_account()
    else:
        print("Oke. Dann legen wir dir kein neues Benutzerkonto an")


def change_username_and_password():
    with open('userdata.pkl', 'rb') as userdata:
        loaded_dict = pickle.load(userdata)
    veränderung_benutzer = eingabe("Möchtest du deinen Benutzernamen und Passwort ändern? ")
    if veränderung_benutzer is None:
        return
    veränderung_benutzer = veränderung_benutzer.strip().lower()
    if veränderung_benutzer in ["ja", "j", "yes", "jo", "klar", "ju"]: # Hier wird sichergegangen dass der User seine Angaben verändern will
        überprüfung_veränderung_benutzer = str(eingabe("Gib bitte zuerst deinen alten Benutzername ein: ")) # Damit auch der Richtige Benutzer geändert wird, Fragen wir nach Benutzername und Passwort
        if überprüfung_veränderung_benutzer is None:
            return
        überprüfung_veränderung_passwort = str(eingabe("Und jetzt bitte noch dein Passwort: "))
        if überprüfung_veränderung_passwort is None:
            return
        if überprüfung_veränderung_benutzer in loaded_dict and loaded_dict[überprüfung_veränderung_benutzer] == überprüfung_veränderung_passwort: #Bei dieser Line wird zuerst überprüft, ob der Benutzername vorhanden ist und danach ob das Passwort übereinstimmt
            veränderter_benutzername = str(eingabe("Bitte gib einen neuen Benutzername ein: "))
            if veränderter_benutzername is None:
                return
            veränderter_benutzername = veränderter_benutzername.strip().lower()
            verändertes_passwort = str(eingabe("Bitte gib ein neues Passwort ein: "))
            if verändertes_passwort is None:
                return
            verändertes_passwort = verändertes_passwort.strip()
            del loaded_dict[überprüfung_veränderung_benutzer]   # alten Benutzer entfernen
            loaded_dict[veränderter_benutzername] = verändertes_passwort
            with open('userdata.pkl', 'wb') as userdata:
                pickle.dump(loaded_dict, userdata)
            print("Dein Benutzername und Passwort wurden erfolgreich gespeichert.")
            
        else:
            print("Diese Kombination konnten wir leider nicht finden, probier es bitte nochmals.")
            
    else:
        print("Dann wird nichts verändert.")

def delete_user():
    loeschen_antwort = eingabe("Möchtest du deinen Account wirklich löschen? ")
    if loeschen_antwort is None:
        return
    loeschen_antwort = loeschen_antwort.strip().lower()
    if loeschen_antwort in ["ja", "j", "yes", "jo", "klar", "ju"]:
        loeschen_name = eingabe("Alles klar. Welchen Account möchstest du löschen? ")
        if loeschen_name is None:
            return
        loeschen_name = loeschen_name.strip()
        if loeschen_name in loaded_dict:
            loeschen_passwort = eingabe("Gebe zur endgültigen Löschung dein Passwort ein: ")
            if loeschen_passwort is None:
                return
            if loeschen_passwort == loaded_dict[loeschen_name]:
                del loaded_dict[loeschen_name]
                print(f"Dein Account {loeschen_name} wurde gelöscht.")
            else:
                print("Falsches Passwort. Der Account wurde nicht gelöscht.")
        else:
            print("Dieser Benutzer wurde nicht gefunden. ")
    else:
        print("Alles klar. Dein Account wurde nicht gelöscht. ")
        