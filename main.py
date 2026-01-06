# Mainprogramm --------------------------------------------------------------------------------------------------------
from ui.registrationframe import start_gui


# "def main()" defines the Mainfunction with which the Project starts. ------------------------------------------------
def main():
    start_gui()


# Ensures that main() is only executed when the script starts directly and not during import.--------------------------
if __name__ == "__main__":
    main()