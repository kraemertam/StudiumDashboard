# StudiumDashboard
Das Projekt "StudiumDashboard" ist eine Desktop-Anwendung zur Verwaltung des eigenen Studienfortschritts. Studierende schreiben sich in einem Kurs ein, sehen alle zugehörigen Modele auf einen Blick und pflegen pro Modul den Status und die Note. 
Das Dashboard errechnet daraus Kennzahlen wie erreichte ETCs, Notendurchschnitt und Fortschritt.

Entstanden ist das Studienprojekt im Rahhmen von "DLBDSOOFPP01_D: Objektorientierte und funktionale Programmierung mit Python". 

## Inhaltsverzeichnis
[Über das Projekt](#über-das-projekt)

## Über das Projekt
### Zielsetzung:
Ziel des StudiumDashboard ist es, einen Überblick über das Studium zu geben und 
laufende Entwicklungen zu erfassen. Gerade beim nebenberuflichen Studium 
läuft man Gefahr, den Überblick zu verlieren. 
Wie ist mein Stand aktuell?
Was steht noch an?

### Funktionsumfang
* Studierende anlegen und in einen Kurs einschreiben (inkl. Notenziel)
* Kurse und Module verwalten, Module einem Kurs zuordnen (mit ETCS-Prüfung gegen das Kurskontigent)
* Modulstatus pflegen: offen, in Bearbeitung, bestanden, nicht bestanden
* Noten erfassen
* Übersichts-Dashboard mit Modulliste & Kennzahlen
* Initialbefüllung der Datenbank aus CSV-Dateien

### Was macht das Projekt?
Mit wenigen Kennzahlen kannst du dir direkt einen Überblick verschaffen.
Mit der Modulübersicht wird dir ein Gesamtüberblick über die unterschiedlichen 
Module deines Studiums gegeben. Welche Module sind mit deinem beruflichen Weg aktuell 
interessant und relevant? Was liegt vor dir? 

### Verwendete Technologien
Als Datenbank wurde SQLite (sqplite3) verwendet.
Die Nutzeroberfläche wurde mit TKinter erstellt.

## Voraussetzungen
* Python 3.11 oder neuer
* die Abhängigkeiten aus requirements.txt
* Getestet unter Windows 11 

## Installation
bash
git clone ....
cd StudiumDashboard

Virtuelle Umgebung anlegen und aktivieren 
python -m venv .venv
.\.venv\Scripts\Activate.ps1

Abhängigkeiten installieren
pip install -r requirements.txt

Datenbank vorbereiten

Anwendung starten
python main.py

Es öffnet sich das Anmeldefenster. Mit den Beispieldaten kann die Studierenden-ID "UI123" zum Ausprobieren verwendet werden. 

## Projektstruktur


## Architektur
Das Proejkt ist in vier Schichten aufgeteilt, die jeweilis nur nach unten hin abhängig sind:
ui -> services -> domains / data

* domains/ ...
* data / ...
* services / ...
* ui/ ...

## Bekannte Einschränkungen
* Keine Benutzerauthentifizierung: Die Anmeldung erfolgt allein über die Studenten-ID
* Einbenutzerbetrieb mit loaler SQLite-Datei, kein gleichzeitiger Zugriff mehrerer Nutzenden
* Modulvoraussetzungen (Modul B setzt Modul A voraus) sind nicht abgebildet
* Keine automatisierten Tests



