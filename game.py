import dice
import random


def start_game():
    print("Die Würfel sind gefallen...")

start_game()

def wuerfel_werfen():                             # Würfeln
    wuerfel = []                                 # leere Liste
    for i in range (5):                          # 5x Würfeln
        wuerfel.append(random.randint(1, 6))    # Würfel zwischen 1 - 6 
    return wuerfel                              # die Würfel werdebn wiedergegeben

wurf = wuerfel_werfen()
print(wurf)

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

def wuerfel_anzeigen(wuerfel_liste):
    for nummer in range(5):
        zeile_text = ""
        for zahl in wuerfel_liste:
            schluessel = ("würfel_" + str(zahl))
            bild = dice.würfel_design[schluessel]
            zeile_text = zeile_text + bild[nummer] + ""
        print(zeile_text)
    buchstaben_wuerfel = ""
    for buchstabe in "ABCDE":
        buchstaben_wuerfel = buchstaben_wuerfel + "    (" + buchstabe + ")    "
    print(buchstaben_wuerfel)


wuerfel_anzeigen(wurf)

#-------------------------DEFINITION ERSTELLT & WÜRFEL MIT BUCHSTABEN VERSEHEN-------------------------#

behalten = input("Welche Würfel möchtest du behalten? (Eingabe mit Buchstaben oder Enter für keinen): ")
behalten = behalten.upper()
print(behalten)