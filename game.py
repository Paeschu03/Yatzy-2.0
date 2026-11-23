import dice
import random
import scorecard

round_number = 0


def start_game():
    ''' Erstellt von Pia '''
    new_scorecard = scorecard.create_scorecard()
    print()
    print("---- SPIEL BEGINNT ----")
    print()

    #Solange spielen, bis alle Kombinationen belegt sind
    while None in new_scorecard.values():
        throw = roll_dice()
        show_dice(throw, "")
        throw = keep_dice(throw)
        result = scorecard.select_category_after_roll(new_scorecard, throw, 3)
        if result is None: 
            return new_scorecard

    print("Alle Kombinationen sind belegt")
    return new_scorecard

def roll_dice():                             # Würfeln
    ''' Erstellt von Pia '''
    dice = []                                # leere Liste
    for i in range (5):                      # 5x Würfeln
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
    ''' Erstellt von Pia '''
    for row in range(5):
        row_text = ""
        for number in dice_list:
            key = ("dice_" + str(number))
            image = dice.dice_design[key]
            row_text = row_text + image[row] + ""
        print(row_text)
    letters_dice = ""
    for letter in "ABCDE":
        if letter in marked:
            letters_dice = letters_dice + "    (" + letter + "*)   "
        else:
            letters_dice = letters_dice + "    (" + letter + ")    "
    print(letters_dice)



#-------------------------DEFINITION ERSTELLT & WÜRFEL MIT BUCHSTABEN VERSEHEN-------------------------#

def keep_dice(dice_list): 
    ''' Erstellt von Pia '''
    for attempt in range(2):
        dice_to_keep = input("Welche Würfel möchtest du behalten? (Eingabe mit Buchstaben oder Enter für keinen): ")
        dice_to_keep = dice_to_keep.upper()
        print(dice_to_keep)
        for index in range(5):
            letter = "ABCDE"[index]
            if letter in dice_to_keep:
                print(letter + " - wird behalten")
            else:
                print(letter + " - wird neu geworfen")
                dice_list[index] = random.randint(1, 6)
        print("Runde ", str(attempt + 2), " von 3")
        show_dice(dice_list, dice_to_keep)
    return dice_list 






#-------------------------WÜRFEL BEHALTEN & ANZEIGEN LASSEN MIT STERN MARKIERT -------------------------#