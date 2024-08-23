import sqlite3

# Connexion à la base de données (elle sera créée si elle n'existe pas)
conn = sqlite3.connect('pointage.db')
c = conn.cursor()

# Création de la table pointage
c.execute('''CREATE TABLE IF NOT EXISTS pointage
             (id INTEGER PRIMARY KEY, nom TEXT, date_arrivee TEXT, heure_arrivee TEXT, heure_depart TEXT)''')

conn.commit()
conn.close()
