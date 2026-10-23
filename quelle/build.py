import json, sys
out = sys.argv[1]
T = ['Obst und Gemüse', 'Bäckerei', 'Kasse']
E = ['🍎', '🥖', '💶']
W = ['BIRNE', 'TORTE', 'KASSE']
START = ['Heute kaufen wir für das Klassenfrühstück ein.', 'Der Supermarkt hat 3 Räume. Jede Tür hat ein Schloss.', 'Tippe auf die Dinge im Raum. Dort warten Aufgaben. Mit dem Code öffnest du die Tür.']
START1 = ['Heute kaufen wir für das Klassenfrühstück ein.', 'Der Supermarkt hat 3 Räume.', 'Drück den Knopf. Dann geht es los.']

N4 = [
 [('Was ist ein Obst?', ['Apfel', 'Gurke', 'Kartoffel', 'Möhre']),
  ('Was ist ein Gemüse?', ['Paprika', 'Banane', 'Kirsche', 'Birne']),
  ('Ein Apfel kostet 50 Cent. Wie viel kosten 2 Äpfel?', ['1 Euro', '50 Cent', '2 Euro', '1,50 Euro']),
  ('Was machst du mit Obst vor dem Essen?', ['Waschen', 'Kochen', 'Braten', 'Backen']),
  ('Wo liegen im Supermarkt die Bananen?', ['Bei Obst und Gemüse', 'Bei den Getränken', 'Bei der Tiefkühlkost', 'Bei den Putzmitteln'])],
 [('Was kaufst du in der Bäckerei?', ['Brötchen', 'Wurst', 'Käse', 'Milch']),
  ('Wer verkauft dir in der Bäckerei das Brot?', ['Die Verkäuferin', 'Die Ärztin', 'Die Friseurin', 'Die Malerin']),
  ('Ein Brot kostet 3 Euro. Du gibst 5 Euro. Wie viel bekommst du zurück?', ['2 Euro', '3 Euro', '1 Euro', '8 Euro']),
  ('Was sagst du höflich an der Theke?', ['Ich hätte gern ein Brot.', 'Gib mir sofort ein Brot.', 'Brot her, aber schnell.', 'Ich nehme mir ein Brot.']),
  ('Was schmeckt süß?', ['Kuchen', 'Brezel', 'Vollkornbrot', 'Laugenstange'])],
 [('Wo bezahlst du im Supermarkt?', ['An der Kasse', 'Am Eingang', 'Im Lager', 'Am Regal']),
  ('Was legst du an der Kasse auf das Band?', ['Die Einkäufe', 'Die Jacke', 'Den Schlüssel', 'Das Handy']),
  ('Milch kostet 1 Euro. Brot kostet 2 Euro. Wie viel kostet alles?', ['3 Euro', '2 Euro', '4 Euro', '1 Euro']),
  ('Was bekommst du nach dem Bezahlen?', ['Den Kassenbon', 'Die Einkaufsliste', 'Den Prospekt', 'Das Preisschild']),
  ('Was sagst du zum Schluss an der Kasse?', ['Danke und tschüss', 'Bis morgen früh', 'Guten Appetit', 'Gute Besserung'])],
]
N3 = [
 [('Was ist Obst?', ['🍎 Apfel', '🥒 Gurke', '🥔 Kartoffel']),
  ('Was ist gelb?', ['🍌 Banane', '🍅 Tomate', '🥦 Brokkoli']),
  ('Was ist Gemüse?', ['🥕 Möhre', '🍓 Erdbeere', '🍐 Birne']),
  ('Was brauchst du zum Einkaufen?', ['💶 Geld', '🎫 Ticket', '🔑 Schlüssel']),
  ('Wie viele Äpfel sind das? 🍎🍎🍎', ['drei', 'zwei', 'vier'])],
 [('Was gibt es beim Bäcker?', ['🥨 Brezel', '🧀 Käse', '🐟 Fisch']),
  ('Was ist süß?', ['🍰 Kuchen', '🥨 Brezel', '🍞 Brot']),
  ('Wie viele Brezeln sind das? 🥨🥨', ['zwei', 'eins', 'drei']),
  ('Wer arbeitet in der Bäckerei?', ['👩‍🍳 Bäckerin', '👩‍⚕️ Ärztin', '👮‍♀️ Polizistin']),
  ('Was sagst du zum Schluss?', ['🙂 Danke', '👋 Hallo', '🎂 Alles Gute'])],
 [('Wo bezahlst du?', ['💶 Kasse', '🚪 Tür', '🗄️ Regal']),
  ('Womit bezahlst du?', ['💶 Geld', '📄 Papier', '🔑 Schlüssel']),
  ('Wie viele Euro sind das? 💶💶💶', ['drei', 'zwei', 'vier']),
  ('Was bekommst du an der Kasse?', ['🧾 Kassenbon', '📰 Zeitung', '✉️ Brief']),
  ('Was sagst du zuerst?', ['👋 Hallo', '🌙 Gute Nacht', '🎂 Alles Gute'])],
]
N2 = [
 [('Apfel', '🍎', '🥕 Möhre'), ('Banane', '🍌', '🍅 Tomate'), ('Birne', '🍐', '🥒 Gurke'), ('Möhre', '🥕', '🍇 Trauben'), ('Erdbeere', '🍓', '🥦 Brokkoli')],
 [('Brot', '🍞', '🧀 Käse'), ('Brezel', '🥨', '🥛 Milch'), ('Croissant', '🥐', '🐟 Fisch'), ('Kuchen', '🍰', '🥚 Ei'), ('Keks', '🍪', '🍗 Hähnchen')],
 [('Geld', '💶', '🔑 Schlüssel'), ('Einkaufswagen', '🛒', '🚲 Fahrrad'), ('Kassenbon', '🧾', '📰 Zeitung'), ('Tasche', '🛍️', '☂️ Schirm'), ('Portemonnaie', '👛', '🧤 Handschuh')],
]
ART = {'Apfel':'der','Banane':'die','Birne':'die','Möhre':'die','Erdbeere':'die','Brot':'das','Brezel':'die','Croissant':'das','Kuchen':'der','Keks':'der','Geld':'das','Einkaufswagen':'der','Kassenbon':'der','Tasche':'die','Portemonnaie':'das'}

FARBEN = [
 {'wand': '#e3edd5', 'seite': '#d2e0c0', 'decke': '#f1f5ea', 'holz': '#b98a5a', 'innen': '#efe3cf', 'tuer': '#7a8f5a'},
 {'wand': '#f3e3cc', 'seite': '#e6d2b5', 'decke': '#f8f0e4', 'holz': '#a9774a', 'innen': '#f6ead8', 'tuer': '#9a6a3f'},
 {'wand': '#dbe6f1', 'seite': '#c8d7e6', 'decke': '#eef3f8', 'holz': '#9fa8b3', 'innen': '#eef1f4', 'tuer': '#5b7896'},
]
def room(i, aufgaben, code):
    return {'titel': T[i], 'emoji': E[i], 'code': code, 'dinge': [e for w, e, d in N2[i]], 'farben': FARBEN[i], 'aufgaben': aufgaben}

lv = {}
lv[4] = [room(i, [{'frage': f, 'antworten': a} for f, a in N4[i]], list(W[i])) for i in range(3)]
lv[3] = [room(i, [{'frage': f, 'antworten': a} for f, a in N3[i]], list(W[i])) for i in range(3)]
lv[2] = [room(i, [{'frage': 'Wo ist %s %s?' % (ART[w].capitalize() if False else ART[w], w), 'antworten': [e + ' ' + w, d]} for w, e, d in N2[i]], [e for w, e, d in N2[i]]) for i in range(3)]
lv[1] = [room(i, [{'frage': 'Da ist %s %s.' % (ART[w], w), 'antworten': [e + ' ' + w]} for w, e, d in N2[i]], [e for w, e, d in N2[i]]) for i in range(3)]

names = {1: 'Niveau 1 – basal', 2: 'Niveau 2 – Symbole', 3: 'Niveau 3 – erstes Lesen', 4: 'Niveau 4 – Lesen und Schreiben'}
cfg = {1: (40, 'false' if False else 'true', 260, 160), 2: (34, 'true', 260, 170), 3: (28, 'false', 220, 120), 4: (24, 'false', 300, 90)}
import os
eng = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'engine.html')).read()
# sanity checks
txt = json.dumps(lv, ensure_ascii=False)
assert "'" not in txt and '\\"' not in txt and '„' not in txt and '“' not in txt
for l, rs in lv.items():
    for r in rs:
        assert len(r['aufgaben']) == 5 and len(r['code']) == 5, (l, r['titel'])
        assert len(set(r['code'])) == 5 or l >= 3
        n = {4: 4, 3: 3, 2: 2, 1: 1}[l]
        assert all(len(a['antworten']) == n for a in r['aufgaben'])
for l in range(1, 5):
    fs, t, minw, btnh = cfg[l]
    h = (eng.replace('__TITLE__', names[l]).replace('__FS__', str(fs)).replace('__MINW__', str(minw)).replace('__BTNH__', str(btnh))
         .replace('__LEVEL__', str(l)).replace('__TON__', t)
         .replace('__START__', json.dumps(START1 if l == 1 else START, ensure_ascii=False))
         .replace('__DATA__', json.dumps(lv[l], ensure_ascii=False, indent=1)))
    assert 'onclick' not in h and '__' not in h
    open(f'{out}/niveau{l}.html', 'w').write(h)
print('ok')
