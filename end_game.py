# Am Spielende wird gefragt ob gespeichert werden soll
# Gäste speichern keinen Spielstand
# user ist der Benutzername, Gäste sind `None`
# score sind die Punkte der Spielrunde
# statistic ist das Dictionary mit den Punktelisten

from input_handling import get_input 

def end_game(user, score, statistics):
    if user is None: 
        print("Als Gast wird kein Spielstand gespeichert")
    else:
        answer = get_input("Möchtest du das Spiel speichern? ")
        if answer is None:
            return
        answer = answer.strip().lower()
        if answer in ["ja", "j", "yes", "jo", "klar", "ju"]:
            if user not in statistics:
                statistics[user] = []
            statistics[user].append(score)
            print("Dein Spielstand wurde erfolgreich gespeichert.")
        else:
            print("Dein Spielstand wurde nicht gespeichert.")

#eventuell lieber if username ==...
if __name__ == "__main__":
    statistics = {"Pia": [180], "Anna": [210]}

    # end_game(None, 250, statistic)

    # end_game("Pia", 120, statistic)
    
    username = input("Mit welchem Benutzernamen spielst du? Bitte leer lassen und Enter drücken, wenn du als Gast spielen möchtest ").strip()
    if username == "":
        username = None 
    end_game(username, 100, statistics)
    print(statistics)