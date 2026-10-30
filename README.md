# Installationsanleitung

## Voraussetzungen

Python 3.14 oder höher ist erforderlich.

## Installation

Klonen Sie das Repository.

```sh
git clone https://github.com/LiZardFox/studium_python_dashboard.git
```

Öffnen Sie eine Kommandozeile und führen Sie die folgenden Befehle aus:

### Erstellen und Aktivieren der Virtuellen Umgebung

```sh
cd studium_python_dashboard
```

```sh
python -m venv .venv && .venv\Scripts\activate.bat
```

### Installierung 

```sh
pip install -e .
```

### Initialisieren der Datenbank

```sh
flask --app study_dash init-db
```

### Laden der Beispieldaten in die Datenbank

```sh
flask --app study_dash load-data
```

### Starten der Anwendung
```sh
flask --app study_dash run
```

Die Anwendung ist nun unter [http://127.0.0.1:5000](http://127.0.0.1:5000) erreichbar.


## Anmeldeinformationen für den Zugriff auf das Dashboard

Matrikelnr: IU123456789

Passwort: password123