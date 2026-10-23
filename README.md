# Escape-Game: Einkaufen

Differenziertes Escape-Game für die Förderschule. Alle Schüler:innen spielen dasselbe Abenteuer mit 3 Räumen (🍎 Obst und Gemüse, 🥖 Bäckerei, 💶 Kasse), jede:r auf dem eigenen Niveau.

Jeder Raum ist als gezeichneter Raum dargestellt. Die Schüler:innen tippen auf 5 Gegenstände (Kiste, Regal links, Tisch, Regal rechts, Korb), lösen dort Aufgaben und sammeln so den Code für die Tür.

| Datei | Niveau | So wird gespielt |
|---|---|---|
| `niveau1.html` | ● basal | Ein großer Knopf, Ursache-Wirkung, kein Richtig und Falsch |
| `niveau2.html` | ●● Symbole | 2 Bild-Antworten, Vorlesen, Bild-Code antippen |
| `niveau3.html` | ●●● erstes Lesen | 3 Antworten mit Emoji, Buchstaben-Kacheln antippen |
| `niveau4.html` | ●●●● Lesen und Schreiben | 4 Antworten, Codewort schreiben |

`index.html` ist die Startseite zur Auswahl des Niveaus.

Jede Niveau-Datei ist in sich geschlossen und funktioniert auch einzeln, zum Beispiel in der App HTML-Klick.

Codewörter (Niveau 3 und 4): BIRNE, TORTE, KASSE.

Die Vorlage, mit der weitere Spiele erzeugt werden können, liegt in `vorlage/prompt-escape-game.md`.

## Spiel ändern

Die Spiel-Logik liegt in `quelle/engine.html`, die Aufgaben in `quelle/build.py`. Nach einer Änderung neu erzeugen mit:

```
python3 quelle/build.py .
```
