def einloggen(konten):
# konten ist ein Dictionary: Benutzername -> Passwort.
while True:
    name = input("Benutzername (X = zurueck): ")
    if name == "X" or name == "x":
        return None
    passwort = input("Passwort (X = zurueck): ")
    if passwort == "X" or passwort == "x":
        return None
    # Erst prüfen, ob der Benutzername existiert, dann darauf zugreifen.
    if name in konten and konten[name] == passwort:
        return name
    print("Ungültiger Benutzername oder Passwort.")