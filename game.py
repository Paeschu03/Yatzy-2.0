import dice
import random
import scorecard

round_number = 0


def start_game():
    #Nur einmal pro Spielrunde erstelen 
    scorecard = scorecard.create_scorecard()
    print()
    print("---- SPIEL BEGINNT ----")
    print()

    #Solange spielen, bis alle Kombis belegt sind
    while None in scorecard.values():
        throw = roll_dice()
        show_dice(throw, "")
        throw = keep_dice(throw)
        result = scorecard.choice_after_roll(scorecard, throw, 3)
        if result is None: 
            return scorecard

    print("Alle Kombinationen sind belegt")
    return scorecard

def roll_dice():                           # Würfeln
    dice = []                                # leere Liste
    for i in range (5):                         # 5x Würfeln
        dice.append(random.randint(1, 6))    # Würfel zwischen 1 - 6 
    return dice                              # die Würfel werdebn wiedergegeben


# print(wurf)                                   wenn wir die Zahl der würfel sehen möchten

#-------------------------5 WÜRFEL KÖNNEN GEWORFEN WERDEN-------------------------#

# print(wurf[0])      # einzelner Würfel aus der Liste holen
# schluessel = ("würfel_" + str(wurf[0]))
# bild = dice.würfel_design[schluessel]
# for zeile in bild:
#    print(zeile)

#-------------------------WÜRFELBILD AUS DICE.PY WIRD ANGEZEIGT-------------------------#

#for zahl in wurf:
#    schluessel = ("würfel_" + str(zahl))
#    bild = dice.würfel_design[schluessel]
#    for zeile in bild:
#        print(zeile)

#-------------------------WÜRFELBILDER ALS FOR SCHLEIFE (KÜRZERER CODE ALS ALLE EINZELN)-------------------------#

#zeile_text = ""
#for zahl in wurf:
#    schluessel = ("würfel_" + str(zahl))
#    bild = dice.würfel_design[schluessel]
#    zeile_text = zeile_text + bild[0] + ""
#print(zeile_text)

#-------------------------ERSTE ZEILE VON 5 WÜRFELN NEBENEINANDER WIRD AUSGEGEBN-------------------------#

# for nummer in range(5):
#   zeile_text = ""
#   for zahl in wurf:
#       schluessel = ("würfel_" + str(zahl))
#       bild = dice.würfel_design[schluessel]
#       zeile_text = zeile_text + bild[nummer] + ""
#           print(zeile_text)

#-------------------------ALLE ZEILEN VON 5 WÜRFELN NEBENEINANDER WERDEN AUSGEGEBEN-------------------------#

def show_dice(dice_list, marked):
    for number in range(5):
        row_text = ""
        for number in dice_list:
            key = ("dice_" + str(number))
            image = dice.dice_design[key]
            row_text = row_text + image[number] + ""
        print(row_text)
    letters_dice = ""
    for letter in "ABCDE":
        if letter in marked:
            letters_dice = letters_dice + "    (" + letter + "*)   "
        else:
            letters_dice = letters_dice + "    (" + letter + ")    "
    print(letters_dice)



#-------------------------DEFINITION ERSTELLT & WÜRFEL MIT BUCHSTABEN VERSEHEN-------------------------#

def wuerfe_behalten(wuerfel_liste): 
    for versuch in range(2):
        behalten = input("Welche Würfel möchtest du behalten? (Eingabe mit Buchstaben oder Enter für keinen): ")
        behalten = behalten.upper()
        print(behalten)
        for platz in range(5):
            buchstabe = "ABCDE"[platz]
            if buchstabe in behalten:
                print(buchstabe + " - wird behalten")
            else:
                print(buchstabe + " - wird neu geworfen")
                wuerfel_liste[platz] = random.randint(1, 6)
        print("Runde ", str(versuch + 2), " von 3")
        wuerfel_anzeigen(wuerfel_liste , behalten)
    return wuerfel_liste 






#-------------------------WÜRFEL BEHALTEN & ANZEIGEN LASSEN MIT STERN MARKIERT -------------------------#