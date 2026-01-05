# Hauptprogramm
from ui.registrationframe import start_gui


# def main() definiert die Hauptfunktion, in der das Projekt startet.
def main():
    start_gui()



# Sorgt dafür, dass main() nur ausgeführt wird, wenn das Skript direkt startet und nicht bereits beim Import.
if __name__ == "__main__":
    main()