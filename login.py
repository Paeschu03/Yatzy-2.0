import pickle 
import menues
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



# loaded_user_data = {"anna": "1234", "ben": "geheim"}
# with open('userdata.pkl', 'wb') as userdata:
 #   pickle.dump(loaded_user_data, userdata)

def laden_kontodaten():
      with open('userdata.pkl', "rb") as f:
         return pickle.load(f)

def login(): 
   logindaten = laden_kontodaten()

   name = input("Benutzernamen: ")
   passwort = input("Passwort: ")

   if name in logindaten and logindaten[name] == passwort:
         print("Hallo ", name, " Sie sind erfolgreich eingeloggt" )

   else:
      neuer_versuch = input("Passwort oder Benutzernamen stimmen nicht! Nochmals versuchen? Ja / Nein: ")
      if neuer_versuch == "Ja":
          login()
      else:
          menues.startausgabe()
          
     
    
 
  



