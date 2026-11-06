from hilfsfunktionen import eingabe

import pickle 
loaded_user_data = {"anna": "1234", "ben": "geheim"}
with open('userdata.pkl', 'wb') as userdata:
    pickle.dump(loaded_user_data, userdata)

with open('userdata.pkl', 'rb') as userdata:
   loaded_dict = pickle.load(userdata)



def account_erstellen():
    neuer_benutzer = eingabe("Möchtest du einen neuen Benutzer anlegen? ")
    if neuer_benutzer is None:
        return
    neuer_benutzer = neuer_benutzer.strip().lower()
    if neuer_benutzer in ["ja", "j", "yes", "jo", "klar", "ju"]:
        neuer_name = eingabe("Oke. Dann gebe nun deinen gewünschten Benutzernamen ein: ")
        if neuer_name is None:
            return
        neuer_name = neuer_name.strip()
        neues_passwort = eingabe("Gebe nun ein Passwort ein: ")
        if neues_passwort is None:
            return
        loaded_dict[neuer_name] = neues_passwort
        print(f"Dein Benutzerkonto mit dem Benutzernamen {neuer_name} und dem Passwort {neues_passwort} wurden nun angelegt.")
        #print(benutzer)
    else:
        print("Oke. Dann legen wir dir kein neues Benutzerkonto an")


def change_username_and_password():
    with open('userdata.pkl', 'rb') as userdata:
        loaded_dict = pickle.load(userdata)
    veränderung_benutzer = eingabe("Möchtest du dein Benutzername und Passwort ändern? ")
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
            verändertes_passwort = verändertes_passwort.strip().lower()
            loaded_dict[veränderter_benutzername] = verändertes_passwort # Hier sollte der alte Benutzername und das alte Passwort überschrieben werden.
            with open('userdata.pkl', 'ab') as userdata:
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
        if loeschen_name in benutzer:
            loeschen_passwort = eingabe("Gebe zur endgültigen Löschung dein Passwort ein: ")
            if loeschen_passwort is None:
                return
            if loeschen_passwort == benutzer[loeschen_name]:
                del benutzer[loeschen_name]
                print(f"Dein Account {loeschen_name} wurde gelöscht.")
            else:
                print("Falsches Passwort. Der Account wurde nicht gelöscht.")
        else:
            print("Dieser Benutzer wurde nicht gefunden. ")
    else:
        print("Alles klar. Dein Account wurde nicht gelöscht. ")
        