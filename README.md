# StudiumDashboard
Das Projekt "StudiumDashboard" ist eine Desktop-Anwendung zur Verwaltung des eigenen Studienfortschritts. Studierende schreiben sich in einem Kurs ein, sehen alle zugehörigen Module auf einen Blick und pflegen pro Modul den Status und die Note. Das Dashboard errechnet daraus Kennzahlen wie erreichte ETCs, Notendurchschnitt und Fortschritt.

Entstanden ist das Studienprojekt im Rahhmen von "DLBDSOOFPP01_D: Objektorientierte und funktionale Programmierung mit Python". 

## Inhaltsverzeichnis 
- [StudiumDashboard](#studiumdashboard)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Über das Projekt](#über-das-projekt)
    - [Zielsetzung:](#zielsetzung)
    - [Funktionsumfang](#funktionsumfang)
    - [Verwendete Technologien](#verwendete-technologien)
  - [Voraussetzungen](#voraussetzungen)
  - [Installation](#installation)
  - [Projektstruktur](#projektstruktur)
  - [Architektur](#architektur)
  - [Bekannte Einschränkungen](#bekannte-einschränkungen)

## Über das Projekt
### Zielsetzung:
Ziel des StudiumDashboard ist es, einen Überblick über das Studium zu geben und den Fortschritt zu erfassen. Gerade beim nebenberuflichen Studium läuft man Gefahr, den Überblick zu verlieren: Wie ist mein aktueller Stand? Welche Module sind noch offen? Liege ich im Rahmen meines Notenziels? Das Dashboard soll einen Überblick schaffen und dich dabei unterstützen.

### Funktionsumfang
* Studierende registrieren und in einen Kurs einschreiben (inkl. Notenziel)
* Modulstatus pflegen: offen, in Bearbeitung, bestanden, nicht bestanden
* Noten erfassen, mit automatischer Statusanpassung
* Übersichts-Dashboard mit Modulübersicht, Kreisdiagramm und Kennzahlen (erreichte ECTS, Notendurchschnitt, Abgleich mit dem Notenziel)
* Kurse und Module über CSV-Dateien anlegen, inklusive ECTS-Prüfung gegen das Kurskontingent
* Automatische Initialbefüllung der Datenbank beim ersten Start

### Verwendete Technologien
* Python 3.11+
* SQLite (`sqlite3`) als Datenbank
* Tkinter für die Benutzeroberfläche
* matplotlib für das Kreisdiagramm, Pillow für Bilder

## Voraussetzungen
* Python 3.11 oder neuer
* die Abhängigkeiten aus requirements.txt
* getestet unter Windows 11 

## Installation

**1. Projekt herunterladen**
```
git clone https://github.com/kraemertam/StudiumDashboard.git
cd StudiumDashboard
```
Ohne Git: auf GitHub „Code → Download ZIP“, entpacken und im Ordner StudiumDashboard ein Terminal öffnen.

**2. Virtuelle Umgebung anlegen und aktivieren (PowerShell)**
```
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```
**3. Abhängigkeiten installieren**
```
pip install -r requirements.txt
```

**4. Anwendung starten**
```
python main.py
```

Beim ersten Start werden die Datenbank sowie Beispieldaten (4 Studiengänge mit Modulen und 3 Studierende) automatisch angelegt. Zum Testen mit der Matrikelnummer IU1111 anmelden oder über „Noch nicht registriert?“ einen eigenen Studenten anlegen.

**Daten ergänzen oder zurücksetzen:** Kurse und Module lassen sich in setup/initial_data_csv/ ergänzen. Nach dem Löschen von data/databank.db wird die Datenbank beim nächsten Start neu aufgebaut.

## Projektstruktur
```
StudiumDashboard/
├── main.py              Startpunkt der Anwendung
├── controller/          Steuerung der Abläufe
├── data/                Repositories und Datenbank
├── domains/             Fachklassen und -regeln
├── services/            Berechnung der Kennzahlen
├── ui/                  Tkinter-Oberfläche
├── setup/               Import der Beispieldaten und CSV-Dateien
└── requirements.txt
```

## Architektur
Das Projekt ist in fünf Schichten aufgeteilt, deren Abhängigkeiten nur von oben nach unten verlaufen:
UI → Controller → Service bzw. Repository

* `ui/` stellt die Ansichten dar und nimmt Eingaben entgegen.
* `controller/` steuert die Abläufe, lädt Daten über die Repositories und wandelt sie in Domain-Objekte um.
* `services/` berechnet die Kennzahlen des Dashboards ohne eigenen Datenbankzugriff.
* `data/` kapselt den Zugriff auf SQLite und liefert einfache Werte zurück.
* `domains/` enthält die fachlichen Klassen und Regeln und kennt keine andere Schicht.

## Bekannte Einschränkungen
* Keine Benutzerauthentifizierung: Die Anmeldung erfolgt allein über die Studenten-ID(Matrikelnummer)
* Einbenutzerbetrieb mit loaler SQLite-Datei, kein gleichzeitiger Zugriff mehrerer Nutzenden
* Werden einem Kurs nachträglich Module hinzugefügt, erscheinen sie nicht bei bereits eingeschriebenen Studierenden.
* Modulvoraussetzungen (Modul B setzt Modul A voraus) sind nicht abgebildet
* Keine automatisierten Tests
