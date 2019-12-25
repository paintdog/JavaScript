import os
import webbrowser

from bs4 import BeautifulSoup


html = '''<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Liste aller HTML-Seiten</title>
  </head>
  <body>
    <p id="summary">Die Datei enthält eine Liste aller HTML-Seiten im Verzeichnis.</p>

    <p>Folgende HTML-Seiten sind vorhanden:</p>

    <table style="border: 1px solid Black;" width="100%">
    <tr>
      <th style="border: 1px solid Black;">Seite</th>
      <th style="border: 1px solid Black;">Beschreibung</th>
    </tr>
    {}
    </table>
  </body>
</html>'''

files_1 = [file for file in os.listdir() if file.endswith(".html") and file.startswith("__")]

files_2 = [file for file in os.listdir() if file.endswith(".html") and not file.startswith("__")]

files = []
files.extend(files_1)
files.extend(files_2)

elemente = []

item = '<tr><td style="border: 1px solid Black;"><a href="{}">{}</a></td><td style="border: 1px solid Black;">{}</td></tr>'

for file in files:

    print(file)

    with open(file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup("\n".join(f.readlines()), "html5lib")

    summary = soup.find("p", {"id": "summary"})

    elemente.append(item.format(file, file, summary.text))

with open("__index__.html", "w", encoding="utf-8") as f:
    f.write(html.format("\n".join(elemente)))

webbrowser.open("__index__.html")
