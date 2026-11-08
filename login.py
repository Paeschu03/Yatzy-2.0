#def einloggen(konten)
# konten ist ein Dictionary: Benutzername -> Passwort.
#while True:
#    name = input("Benutzername (X = zurueck): ")
#    if name == "X" or name == "x":
#    return None

#hier kann der Benutzer sich einloggen 
#Aus dem Speicherfile wird hier überprüft. 

#in diese Methode muss minimum Benutzernamen und Passwort mitgegeben werden
#Ist der Benutzer korrekt eingeloggt, wird er von hier zu menues geleitet. Dort wird er gefragt was er als eingeloggter Spieler machen will. 

#Funktioniert das Login nicht, kann er solang probieren, bis es funktioniert 

#Will er abbrechen, so kommt er von hier zum menues.py zur startausgabe zurück. 
#test

import pickle 
from hilfsfunktionen import eingabe
# loaded_user_data = {"anna": "1234", "ben": "geheim"}
# with open('userdata.pkl', 'wb') as userdata:
 #   pickle.dump(loaded_user_data, userdata)
def einloggen():
    # Neu lesen, damit neu erstellte/geänderte Konten berücksichtigt werden.
    with open("userdata.pkl", "rb") as userdata:
        konten = pickle.load(userdata)

    print()
    print("Einloggen")
    print("Mit X kommst du zurück zur Startausgabe zurück.")
   
    while True:
        name = eingabe("Benutzername: ")

        if name is None:
            return None

        name = name.strip()
        passwort = eingabe("Passwort: ")

        if passwort is None:
            return None

        if name in konten and konten[name] == passwort:
            return name

        print("Ungültiger Benutzername oder Passwort.")
        print("Bitte versuche es erneut.")

