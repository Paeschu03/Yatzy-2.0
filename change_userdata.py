# import login 
import menues
import dice
import tutorial



benutzer = {"Pia": "1234", "Anna": "pw" }
# print(benutzer)

neuer_benutzer = input("Möchtest du einen neuen Benutzer anlegen? ").strip().lower()
if neuer_benutzer in ["ja", "j", "yes", "jo", "klar", "ju"]:
    neuer_name = input("Oke. Dann gebe nun deinen gewünschten Benutzernamen ein: ").strip()
    neues_passwort = input("Gebe nun ein Passwort ein: ")
    benutzer[neuer_name] = neues_passwort
    print(f"Dein Benutzerkonto mit dem Benutzernamen {neuer_name} und dem Passwort {neues_passwort} wurden nun angelegt.")
    #print(benutzer)
else:
    print("Oke. Dann legen wir dir kein neues Benutzerkonto an")

def konto_loeschen(benutzer):
    loeschen_antwort = input("Möchtest du deinen Account wirklich löschen? ").strip().lower()
    if loeschen_antwort in ["ja", "j", "yes", "jo", "klar", "ju"]:
        loeschen_name = input("Alles klar. Welchen Account möchstest du löschen? ").strip()
        if loeschen_name in benutzer:
            loeschen_passwort = input("Gebe zur endgültigen Löschung noch dein Passwort ein: ")
            if loeschen_passwort == benutzer[loeschen_name]:
                del benutzer[loeschen_name]
                print(f"Dein Account {loeschen_name} wurde gelöscht.")
            else:
                print("Falsches Passwort. Der Account wurde nicht gelöscht.")
        else:
            print("Dieser Benutzer wurde nicht gefunden. ")
    else:
        print("Alles klar. Dein Account wurde nicht gelöscht. ")

konto_loeschen(benutzer)