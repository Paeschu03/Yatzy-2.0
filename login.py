import pickle 
import menues

# loaded_user_data = {"anna": "1234", "ben": "geheim"}
# with open('userdata.pkl', 'wb') as userdata:
 #   pickle.dump(loaded_user_data, userdata)



def login():
   #Die gespeicherten Benutzernamen und Passwörter werden geladen.
   with open('userdata.pkl', 'rb') as userdata:
      aktuelle_benutzerliste = pickle.load(userdata)
      print("Login:", userdata)
      
   benutzer = input("Dein Benutzernamen: ")
   passwort = input("Dein Passwort: ")

   if benutzer not in aktuelle_benutzerliste:
      print("Den Benutzernamen '", benutzer, "'konnte nicht gefunden werden")
      nochmals = input("Verschrieben? Ja / Nein ")
      if nochmals == "Ja":
         login()
      if nochmals != "Nein":
         menues.startausgabe

   if aktuelle_benutzerliste[benutzer] != passwort: 
      print("Falsches Passwort")
      return

   if aktuelle_benutzerliste[benutzer] == passwort: 
      print("Sie sind erfolgreich eingeloggt")
      menues.menue_mit_account()


