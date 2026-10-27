# Am Spielende wird gefragt ob gespeichert werden soll
# Gäste speichern keinen Spielstand
# user ist der Benutzername, Gäste sind `None`
# score sind die Punkte der Spielrunde
# statistic ist das Dictionary mit den Punktelisten

def end_game(user, score, statistic):
    if user is None: 
        print("Als Gast wird kein Spielstand gespeichert")
    else:
        answer = input("Möchtest du das Spiel speichern? ").strip().lower()
        if answer in ["ja", "j", "yes", "jo", "klar", "ju"]:
            if user not in statistic:
                statistic[user] = []
            statistic[user].append(score)
            print("Dein Spielstand wurde erfolgreich gespeichert.")
        else:
            print("Dein Spielstand wurde nicht gespeichert.")

if __name__ == "__main__":
    statistic = {"Pia": [180], "Anna": [210]}

    # end_game(None, 250, statistic)

    # end_game("Pia", 120, statistic)
    
    name = input("Mit welchem Benutzernamen spielst du? Bitte leer lassen und Enter drücken, wenn du als Gast spielst ").strip()
    if name == "":
        name = None 
    end_game(name, 100, statistic)
    print(statistic)