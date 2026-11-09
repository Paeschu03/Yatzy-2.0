def eingabe(text):
    abbrechen = input(text)
    if abbrechen.strip().lower() == "x":
        return None
    return abbrechen

if __name__ == "__main__":
    print(eingabe("Test: "))