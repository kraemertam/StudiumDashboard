from openpyxl import load_workbook
import data.Students


id = input("Gib hier deine id ein:")


def login_check(id):
    filename = str("data/Students" + id + ".csv")
    print(filename)
    try:
        with open(str(filename), "r") as studentfile:
            print("File open")
    except:
        print("Datei ist nicht vorhanden")

login_check(id)