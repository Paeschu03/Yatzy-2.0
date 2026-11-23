def get_input(text):
    ''' Erstellt von Pia '''
    cancel = input(text)
    if cancel.strip().lower() == "x":
        return None
    return cancel

if __name__ == "__main__":
    print(get_input("Test: "))