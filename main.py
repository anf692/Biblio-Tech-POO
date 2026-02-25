from bibliothecaire import Bibliothecaire
from livre import Livre
from magazine import Magazine

class Application:
    """Classe principale de l'application de gestion de bibliothèque."""

    def __init__(self):
        self.bibliothecaire = Bibliothecaire()

    def lancer(self):
        """Lance l'application et affiche le menu principal."""
        while True:
            print("\n===== MENU =====")
            print("1. Ajouter un Livre")
            print("2. Ajouter un Magazine")
            print("3. Inscrire un membre")
            print("4. Emprunter un document")
            print("5. Retourner un document")
            print("6. Afficher le catalogue")
            print("7. Afficher les membres")
            print("8. Rechercher un document par titre ou ID")
            print("9. Lister les emprunts d'un membre")
            print("10. Démonstration verrouillage")
            print("11. Quitter")

            choix = input("Votre choix : ")

            try:
                match choix:

                    case "1":
                        try:
                            while True:
                        
                                titre = input("Titre : ").strip().replace(" ", "")

                                if not titre.isalpha():
                                    print("Le titre doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break

                            while True:
                                auteur = input("Auteur : ").strip().replace(" ", "")

                                if not auteur.isalpha():
                                    print("Le nom de l'auteur doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break

                            doc = Livre(titre, auteur)

                            self.bibliothecaire.ajouter_document(doc)
                            print("Livre ajouté avec succès.")

                        except Exception as e:
                            print("Erreur lors de l'ajout du livre :", e)

                    case "2":
                        try:
                            while True:
                                titre = input("Titre : ").strip().replace(" ", "")
                                if not titre.isalpha():
                                    print("Le titre doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break

                            while True:
                                numero = input("Numéro : ").strip().replace(" ", "")
                                if not numero.isdigit():
                                    print("Le numéro doit être composé uniquement de chiffres. Veuillez réessayer.")
                                else:
                                    break

                            doc = Magazine(titre, numero)
                            self.bibliothecaire.ajouter_document(doc)
                            print("Magazine ajouté avec succès.")

                        except Exception as e:
                            print("Erreur lors de l'ajout du magazine :", e)

                    case "3":
                        try:
                            while True:
                                nom = input("Nom du membre : ").strip().replace(" ", "")
                                if not nom.isalpha():
                                    print("Le nom du membre doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break

                            self.bibliothecaire.inscrire_membre(nom)
                            print("Membre inscrit avec succès.")

                        except Exception as e:
                            print("Erreur lors de l'inscription du membre :", e)

                    case "4":
                        try:
                            while True:
                                titre = input("Titre du document à emprunter : ").strip().replace(" ", "")
                                if not titre:
                                    print("Le titre doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break

                            while True:
                                nom = input("Nom membre : ").strip().replace(" ", "")
                                if not nom.isalpha():
                                    print("Le nom du membre doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break

                            self.bibliothecaire.emprunter_document(titre, nom)
                            print("Emprunt validé.")

                        except Exception as e:
                            print("Erreur lors de l'emprunt :", e)

                    case "5":
                        try:
                            while True:
                                titre = input("Titre du document à retourner : ").strip().replace(" ", "")
                                if not titre.isalpha():
                                    print("Le titre doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break

                            while True:
                                nom = input("Nom membre : ").strip().replace(" ", "")
                                if not nom.isalpha():
                                    print("Le nom du membre doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break

                            self.bibliothecaire.retourner_document(titre, nom)
                            print("Retour validé.")
                        except Exception as e:
                            print("Erreur lors du retour :", e)

                    case "6":
                        catalogue = self.bibliothecaire.afficher_catalogue()
                        if not catalogue:
                            print("Catalogue vide.")
                        else:
                            for doc in catalogue:
                                print(doc)

                    case "7":
                        membres = self.bibliothecaire.afficher_membres()
                        if not membres:
                            print("Aucun membre inscrit.")
                        else:
                            for membre in membres:
                                print('- ' + membre)

                    case "8":
                        try:
                            while True:
                                titre = input("Titre ou ID du document : ").strip()
                                if not titre:
                                    print("Le titre ou ID doit être composé uniquement de lettres ou de chiffres. Veuillez réessayer.")
                                else:
                                    break

                            doc = self.bibliothecaire.trouver_document(titre)

                            if doc:
                                print(doc)
                            else:
                                print("Document non trouvé.")

                        except Exception as e:
                            print("Erreur lors de la recherche du document :", e)

                    case "9":
                        try:
                            while True:
                                nom = input("Nom membre : ").strip().replace(" ", "")
                                if not nom.isalpha():
                                    print("Le nom du membre doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break

                            emprunts = self.bibliothecaire.afficher_emprunts_membre(nom)

                            if not emprunts:
                                print("Aucun emprunt pour ce membre.")
                            else:
                                for doc in emprunts:
                                    print(doc)

                        except Exception as e:
                            print("Erreur :", e)

                    case "10":
                        # Démonstration verrouillage
                        livre = Livre("TestVerrou", "AuteurTest")
                        print("Disponible :", livre.disponible)
                        print("Tentative modification sauvage...")
                        try:
                            livre.disponible = False  # doit échouer
                        except AttributeError as e:
                            print("Impossible de modifier directement:", e)

                    case "11":
                        print("Au revoir")
                        break

                    case _:
                        print("Choix invalide.")

            except Exception as e:
                print("Erreur :", e)


app = Application()
app.lancer()