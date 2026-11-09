import dice
import random


def start_game():
    #print("Runde 1 von 3")
    wurf = wuerfel_werfen()
    wuerfel_anzeigen(wurf, "")


def wuerfel_werfen():                           # Würfeln
    wuerfel = []                                # leere Liste
    for i in range (5):                         # 5x Würfeln
        wuerfel.append(random.randint(1, 6))    # Würfel zwischen 1 - 6 
    return wuerfel                              # die Würfel werdebn wiedergegeben


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

def wuerfel_anzeigen(wuerfel_liste, markiert):
    for nummer in range(5):
        zeile_text = ""
        for zahl in wuerfel_liste:
            schluessel = ("wuerfel_" + str(zahl))
            bild = dice.wuerfel_design[schluessel]
            zeile_text = zeile_text + bild[nummer] + ""
        print(zeile_text)
    buchstaben_wuerfel = ""
    for buchstabe in "ABCDE":
        if buchstabe in markiert:
            buchstaben_wuerfel = buchstaben_wuerfel + "    (" + buchstabe + "*)   "
        else:
            buchstaben_wuerfel = buchstaben_wuerfel + "    (" + buchstabe + ")    "
    print(buchstaben_wuerfel)



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


#wurf = wuerfe_behalten(wurf)



#-------------------------WÜRFEL BEHALTEN & ANZEIGEN LASSEN MIT STERN MARKIERT -------------------------#