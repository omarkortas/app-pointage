import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sqlite3

# Fonction pour enregistrer l'heure d'arrivée
def enregistrer_arrivee():
    nom = entry_nom.get()
    date_arrivee = datetime.now().strftime("%Y-%m-%d")
    heure_arrivee = datetime.now().strftime("%H:%M:%S")

    if nom:
        conn = sqlite3.connect('pointage.db')
        c = conn.cursor()
        c.execute("INSERT INTO pointage (nom, date_arrivee, heure_arrivee) VALUES (?, ?, ?)",
                  (nom, date_arrivee, heure_arrivee))
        conn.commit()
        conn.close()

        messagebox.showinfo("Pointage", f"Arrivée enregistrée pour {nom} à {heure_arrivee} le {date_arrivee}.")
        entry_nom.delete(0, tk.END)
    else:
        messagebox.showwarning("Erreur", "Veuillez entrer un nom.")

# Fonction pour enregistrer l'heure de départ
def enregistrer_depart():
    nom = entry_nom.get()
    heure_depart = datetime.now().strftime("%H:%M:%S")

    if nom:
        conn = sqlite3.connect('pointage.db')
        c = conn.cursor()
        c.execute("UPDATE pointage SET heure_depart = ? WHERE nom = ? AND heure_depart IS NULL", (heure_depart, nom))
        conn.commit()
        conn.close()

        messagebox.showinfo("Pointage", f"Départ enregistré pour {nom} à {heure_depart}.")
        entry_nom.delete(0, tk.END)
    else:
        messagebox.showwarning("Erreur", "Veuillez entrer un nom.")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Application de Pointage")

# Label et champ d'entrée pour le nom
label_nom = tk.Label(fenetre, text="Nom:")
label_nom.pack(pady=5)
entry_nom = tk.Entry(fenetre)
entry_nom.pack(pady=5)

# Boutons pour enregistrer l'heure d'arrivée et de départ
bouton_arrivee = tk.Button(fenetre, text="Enregistrer l'Arrivée", command=enregistrer_arrivee)
bouton_arrivee.pack(pady=10)

bouton_depart = tk.Button(fenetre, text="Enregistrer le Départ", command=enregistrer_depart)
bouton_depart.pack(pady=10)


#dev interface 
# Ajout d'un menu à la fenêtre
menu_bar = tk.Menu(fenetre)

# Menu "Fichier"
menu_fichier = tk.Menu(menu_bar, tearoff=0)
menu_fichier.add_command(label="Ouvrir")
menu_fichier.add_command(label="Enregistrer")
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=fenetre.quit)
menu_bar.add_cascade(label="Fichier", menu=menu_fichier)

# Menu "Aide"
menu_aide = tk.Menu(menu_bar, tearoff=0)
menu_aide.add_command(label="À propos")
menu_bar.add_cascade(label="Aide", menu=menu_aide)

# Affichage du menu
fenetre.config(menu=menu_bar)
# Création d'un cadre pour l'entrée du nom
frame_nom = tk.Frame(fenetre)
frame_nom.pack(pady=10)

label_nom = tk.Label(frame_nom, text="Nom:")
label_nom.pack(side=tk.LEFT)
entry_nom = tk.Entry(frame_nom)
entry_nom.pack(side=tk.LEFT)
from tkinter import ttk

# Création d'un notebook (ensemble d'onglets)
notebook = ttk.Notebook(fenetre)
notebook.pack(pady=10, expand=True)

# Création des onglets
onglet_pointage = ttk.Frame(notebook)
onglet_rapports = ttk.Frame(notebook)

notebook.add(onglet_pointage, text='Pointage')
notebook.add(onglet_rapports, text='Rapports')

# Ajout de widgets dans chaque onglet
label_nom_onglet = tk.Label(onglet_pointage, text="Nom:")
label_nom_onglet.pack(pady=5)
entry_nom_onglet = tk.Entry(onglet_pointage)
entry_nom_onglet.pack(pady=5)
# Ajout d'une Combobox (liste déroulante)
label_role = tk.Label(fenetre, text="Rôle:")
label_role.pack(pady=5)
combobox_role = ttk.Combobox(fenetre, values=["Employé", "Manager", "Administrateur"])
combobox_role.pack(pady=5)
# Ajout d'une zone de texte pour les rapports
label_rapport = tk.Label(fenetre, text="Rapports:")
label_rapport.pack(pady=5)
text_rapport = tk.Text(fenetre, height=10, width=50)
text_rapport.pack(pady=5)

# Ajout d'un bouton pour charger les rapports
bouton_charger_rapport = tk.Button(fenetre, text="Charger le Rapport", command=lambda: text_rapport.insert(tk.END, "Rapport chargé..."))
bouton_charger_rapport.pack(pady=10)
# Ajout d'un événement double-clic sur une liste
listbox = tk.Listbox(fenetre)
listbox.pack(pady=5)
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")

def on_double_click(event):
    item = listbox.get(listbox.curselection())
    messagebox.showinfo("Sélection", f"Vous avez sélectionné {item}")

listbox.bind("<Double-Button-1>", on_double_click)
# Changer le titre de la fenêtre
fenetre.title("Application de Pointage Avancée")

# Définir les dimensions minimales de la fenêtre
fenetre.minsize(400, 300)

# Changer l'icône de la fenêtre (remplacez 'icone.ico' par votre propre icône)
fenetre.iconbitmap('icone.ico')



# Lancement de l'application
fenetre.mainloop()
