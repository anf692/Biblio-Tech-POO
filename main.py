from bibliothecaire import Bibliothecaire
from livre import Livre
from magazine import Magazine

class Application:
    def __init__(self):
        self.bibliothecaire = Bibliothecaire()

    def lancer(self):
        while True:
            print("\n===== MENU =====")
            print("1. Ajouter un Livre")
            print("2. Ajouter un Magazine")
            print("3. Inscrire un membre")
            print("4. Emprunter un document")
            print("5. Retourner un document")
            print("6. Afficher le catalogue")
            print("7. Lister les emprunts d'un membre")
            print("8. Démonstration verrouillage")
            print("9. Quitter")

            choix = input("Votre choix : ")

            try:
                match choix:

                    case "1":
                        try:
                            titre = input("Titre : ").strip()
                            auteur = input("Auteur : ").strip()

                            doc = Livre(titre, auteur)
                            self.bibliothecaire.ajouter_document(doc)
                            print("Livre ajouté avec succès.")

                        except Exception as e:
                            print("Erreur lors de l'ajout du livre :", e)

                    case "2":
                        try:
                            titre = input("Titre : ").strip()
                            numero = input("Numéro : ").strip()

                            doc = Magazine(titre, numero)
                            self.bibliothecaire.ajouter_document(doc)
                            print("Magazine ajouté avec succès.")

                        except Exception as e:
                            print("Erreur lors de l'ajout du magazine :", e)

                    case "3":
                        try:
                            nom = input("Nom du membre : ").strip()
                            self.bibliothecaire.inscrire_membre(nom)
                            print("Membre inscrit avec succès.")
                        except Exception as e:
                            print("Erreur lors de l'inscription du membre :", e)

                    case "4":
                        try:
                            titre = input("Titre : ").strip()
                            nom = input("Nom membre : ").strip()
                            self.bibliothecaire.emprunter_document(titre, nom)
                            print("Emprunt validé.")
                        except Exception as e:
                            print("Erreur lors de l'emprunt :", e)

                    case "5":
                        try:
                            titre = input("Titre : ").strip()
                            nom = input("Nom membre : ").strip()
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
                        try:
                            nom = input("Nom membre : ").strip()
                            emprunts = self.bibliothecaire.afficher_emprunts_membre(nom)
                            if not emprunts:
                                print("Aucun emprunt pour ce membre.")
                            else:
                                for doc in emprunts:
                                    print(doc)
                        except Exception as e:
                            print("Erreur :", e)

                    case "8":
                        # Démonstration verrouillage
                        livre = Livre("TestVerrou", "AuteurTest")
                        print("Disponible :", livre.disponible)
                        print("Tentative modification sauvage...")
                        try:
                            livre.disponible = False  # doit échouer
                        except AttributeError as e:
                            print("Impossible de modifier directement:", e)

                    case "9":
                        print("Au revoir")
                        break

                    case _:
                        print("Choix invalide.")

            except Exception as e:
                print("Erreur :", e)


app = Application()
app.lancer()