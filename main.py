taches = []


def afficher_menu():
    print("\n--- Menu ---")
    print("1 - Ajouter une tache")
    print("2 - Afficher les taches")
    print("3 - Rechercher une tache")
    print("0 - Quitter")


def ajouter():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        return
    taches.append(titre)
    print("Tâche ajoutée.")


def afficher():
    if len(taches) == 0:
        print("La liste est vide.")
        return
    for i, t in enumerate(taches, start=1):
        print(f"{i}. {t}")


def rechercher():
    mot = input("Mot-clé : ").strip().lower()
    trouve = False
    for i, t in enumerate(taches, start=1):
        # on compare en minuscules pour ignorer la casse
        if mot in t.lower():
            print(f"{i}. {t}")
            trouve = True
    if not trouve:
        print("Aucune tâche trouvée.")


while True:
    afficher_menu()
    choix = input("Votre choix : ").strip()
    if choix == "1":
        ajouter()
    elif choix == "2":
        afficher()
    elif choix == "3":
        rechercher()
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Erreur : option invalide.")