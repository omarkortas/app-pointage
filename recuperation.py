import sqlite3

# Fonction pour récupérer tous les noms enregistrés
def recuperer_noms():
    conn = sqlite3.connect('pointage.db')
    c = conn.cursor()

    # Exécution de la requête pour sélectionner tous les noms distincts
    c.execute("SELECT DISTINCT nom FROM pointage")
    noms = c.fetchall()  # Récupère tous les résultats de la requête

    conn.close()

    # Retourne une liste de noms
    return [nom[0] for nom in noms]

# Appel de la fonction et affichage des résultats
noms_enregistres = recuperer_noms()
print("Noms enregistrés :")
for nom in noms_enregistres:
    print(nom)
