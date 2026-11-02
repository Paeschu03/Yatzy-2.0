
import pickle 
# loaded_user_data = {"anna": "1234", "ben": "geheim"}
# with open('userdata.pkl', 'wb') as userdata:
 #   pickle.dump(loaded_user_data, userdata)

with open('userdata.pkl', 'rb') as userdata:
   loaded_dict = pickle.load(userdata)



def new_user():
    neuer_benutzer = input("Möchtest du einen neuen Benutzer anlegen? ").strip().lower()
    if neuer_benutzer in ["ja", "j", "yes", "jo", "klar", "ju"]:
        neuer_name = input("Oke. Dann gebe nun deinen gewünschten Benutzernamen ein: ").strip()
        neues_passwort = input("Gebe nun ein Passwort ein: ")
        benutzer[neuer_name] = neues_passwort
        print(f"Dein Benutzerkonto mit dem Benutzernamen {neuer_name} und dem Passwort {neues_passwort} wurden nun angelegt.")
        #print(benutzer)
    else:
        print("Oke. Dann legen wir dir kein neues Benutzerkonto an")


def change_username_and_password():
    with open('userdata.pkl', 'rb') as userdata:
        loaded_dict = pickle.load(userdata)
    veränderung_benutzer = input("Möchtest du dein Benutzername und Passwort ändern? ").strip().lower()
    if veränderung_benutzer in ["ja", "j", "yes", "jo", "klar", "ju"]: # Hier wird sichergegangen dass der User seine Angaben verändern will
        überprüfung_veränderung_benutzer = str(input("Gib bitte zuerst deinen alten Benutzername ein: ")).strip() # Damit auch der Richtige Benutzer geändert wird, Fragen wir nach Benutzername und Passwort
        überprüfung_veränderung_passwort = str(input("Und jetzt bitte noch dein Passwort: ")).strip()
        if überprüfung_veränderung_benutzer in loaded_dict and loaded_dict[überprüfung_veränderung_benutzer] == überprüfung_veränderung_passwort: #Bei dieser Line wird zuerst überprüft, ob der Benutzername vorhanden ist und danach ob das Passwort übereinstimmt
            veränderter_benutzername = str(input("Bitte gib einen neuen Benutzername ein: ")).strip()
            verändertes_passwort = str(input("Bitte gib ein neues Passwort ein: ")).strip()
            loaded_dict[veränderter_benutzername] = verändertes_passwort # Hier sollte der alte Benutzername und das alte Passwort überschrieben werden.
            with open('userdata.pkl', 'ab') as userdata:
                pickle.dump(loaded_dict, userdata)
            print("Dein Benutzername und Passwort wurden erfolgreich gespeichert.")
            
        else:
            print("Diese Kombination konnten wir leider nicht finden, probier es bitte nochmals.")
            
    else:
        print("Dann wird nichts verändert.")

def delete_user():
    loeschen_antwort = input("Möchtest du deinen Account wirklich löschen? ").strip().lower()
    if loeschen_antwort in ["ja", "j", "yes", "jo", "klar", "ju"]:
        loeschen_name = input("Alles klar. Welchen Account möchstest du löschen? ").strip()
        if loeschen_name in benutzer:
            loeschen_passwort = input("Gebe zur endgültigen Löschung dein Passwort ein: ")
            if loeschen_passwort == benutzer[loeschen_name]:
                del benutzer[loeschen_name]
                print(f"Dein Account {loeschen_name} wurde gelöscht.")
            else:
                print("Falsches Passwort. Der Account wurde nicht gelöscht.")
        else:
            print("Dieser Benutzer wurde nicht gefunden. ")
    else:
        print("Alles klar. Dein Account wurde nicht gelöscht. ")
        