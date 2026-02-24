from bibliothecaire import Bibliothecaire
from livre import Livre
from magazine import Magazine

#programme principal
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
                            while True:
                                titre = input("Titre : ").strip().replace(" ", "")

                                if not titre.isalpha():
                                    print("Le titre doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break
                                
                            while True:
                                auteur = input("Auteur : ").strip().replace(" ", "")

                                if not auteur.isalpha() :
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
                                numero = input("Numéro : ").strip()

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
                                titre = input("Titre : ").strip().replace(" ", "")

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

                            self.bibliothecaire.emprunter_document(titre, nom)
                            print("Emprunt validé.")

                        except Exception as e:
                            print("Erreur lors de l'emprunt :", e)

                    case "5":
                        try:
                            while True:
                                titre = input("Titre : ").strip().replace(" ", "")

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
                            raise Exception("Catalogue vide.")

                        # Affiche chaque document avec son statut de disponibilité
                        for doc in catalogue:
                            statut = "Disponible" if doc.disponible else "Indisponible"
                            print("-", doc.titre, "|", statut)

                    case "7":
                        try:
                            while True:
                                nom = input("Nom membre : ").strip().replace(" ", "")
                                if not nom.isalpha():
                                    print("Le nom du membre doit être composé uniquement de lettres. Veuillez réessayer.")
                                else:
                                    break
                        

                            membres = self.bibliothecaire.afficher_membres()

                            # Vérifie que le membre existe et qu'il a des emprunts
                            if nom not in membres:
                                raise Exception("Membre introuvable.")

                            # Vérifie que le membre a des emprunts
                            if not membres[nom]:
                                raise Exception("Aucun emprunt.")

                            # Affiche les titres des documents empruntés par le membre
                            for doc in membres[nom]:
                                print("-", doc.titre)

                        except Exception as e:
                            print("Erreur :", e)

                    case "8":
                        print("\n--- TEST VERROUILLAGE ---")
                        livre = Livre("Test", "Auteur")

                        print("Disponible :", livre.disponible)
                        print("Tentative modification sauvage...")
                        livre.disponible = False  # doit échouer

                    case "9":
                        print("Au revoir")
                        break

                    case _:
                        raise Exception("Choix invalide.")

            except Exception as e:
                print("Erreur :", e)



app = Application()
app.lancer()