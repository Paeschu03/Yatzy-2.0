import pickle 
import menus

# loaded_user_data = {"anna": "1234", "ben": "geheim"}
# with open('userdata.pkl', 'wb') as userdata:
 #   pickle.dump(loaded_user_data, userdata)



def login():
   #Die gespeicherten Benutzernamen und Passwörter werden geladen.
   with open('userdata.pkl', 'rb') as userdata:
      current_user_list = pickle.load(userdata)
      print("Login:", userdata)
      
   username = input("Dein Benutzernamen: ")
   password = input("Dein Passwort: ")

   if username not in current_user_list:
      print("Den Benutzernamen '", username, "'konnte nicht gefunden werden")
      nochmals = input("Verschrieben? Ja / Nein ")
      if nochmals == "Ja":
         login()
      if nochmals == "Nein":
         menus.show_start_menu()
   print(current_user_list)
   if current_user_list[username] != password: 
      print("Falscher Benutzername oder Falsches Passwort")
      login()
      return

   if current_user_list[username] == password: 
      print("Sie sind erfolgreich eingeloggt")
      menus.show_account_menu()


