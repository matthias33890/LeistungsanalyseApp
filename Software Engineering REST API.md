# Simple REST API

## Description

Das folgende Beispiel zeigt, wie man eine einfache REST-API mit Python und Flask-Webservice erstellt. Hierbei können Nutzer:innen mit Email-Adressen und Passwörtern angelegt und authentifiziert werden.

## Requirements

Legen Sie eine neue virutelle Umgebung an und installieren Sie die Requirements.

```bash
pip install -r requirements.txt
```

## Usage

- Starten des Severs im Terminals mittels `python main.py`
- Dieser sollte nun unter `http://127.0.0.1:5000` erreichbar sein
- Nun stehen drei weitere Skripte bereit, mittels derer gezeigt wird, wie sie aus Python heraus mit dem Webservice kommuniziert werden kann 
  - Mittels `put_api.py` können neue User angelegt werden
  - Mittels `post_api.py` können Email-Adressen von Usern geändert oder hinzugefügt werden werden
  - Mittels `get_api.py` können Informationen zu Usern abgerufen werden
