# Diese Datei __init__.py markiert den Ordner als Python-Paket. Python erkennt, dass sich in diesem Ordner importierbarer Code befindet.
# In dieser Datei muss nichts stehen. Du kannst dort aber auch Code unterbringen, der beim Import des Pakets automatisch ausgeführt wird.
# Zum Beispiel:
print("Paket Module wurde geladen")

# In der Praxis nutzt man diese Datei oft, um wichtige Klassen und Funktionen direkt zugänglich zu machen
# from .student_service import Student
# Dann kann du in die andere Dateien direkt schreiben: "from logic import Student" statt den kompletten Pfad "logic.student_service.Student"

from services import beispielmodul