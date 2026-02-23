from abc import ABC, abstractmethod



class Document(ABC):
    """Classe abstraite représentant un document de la bibliothèque."""

    def __init__(self, titre):
        self._titre = titre
        self.__disponible = True #(name mangling)

    @property
    def titre(self):
        return self._titre

    @property
    def disponible(self):
        return self.__disponible

    @abstractmethod
    def emprunter(self):
        """Méthode abstraite à implémenter par les sous-classes."""
        pass

    @abstractmethod
    def retourner(self):
        """Méthode abstraite à implémenter par les sous-classes."""
        pass

    def _changer_disponibilite(self, etat):
        """Méthode protégée pour changer la disponibilité du document."""
        self.__disponible = etat




class Livre(Document):
    """Classe représentant un livre, héritant de Document."""
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self._auteur = auteur

    @property
    def auteur(self):
        """Retourne l'auteur du livre."""
        return self._auteur


    def emprunter(self):
        """methode d'emprunter le livre si disponible."""
        if not self.disponible:
            raise Exception("Livre déjà indisponible.")
        self._changer_disponibilite(False)

    def retourner(self):
        """methode de retourner le livre."""
        self._changer_disponibilite(True)




class Magazine(Document):
    """Classe représentant un magazine, héritant de Document."""
    def __init__(self, titre, numero):
        super().__init__(titre)
        self._numero = numero

    @property
    def numero(self):
        """Retourne le numéro du magazine."""
        return self._numero

    def emprunter(self):
        """methode d'emprunter le magazine si disponible."""
        if not self.disponible:
            raise Exception("Magazine déjà indisponible.")
        self._changer_disponibilite(False)


    def retourner(self):
        """methode de retourner le magazine."""
        self._changer_disponibilite(True)



class Bibliothecaire:
    """Classe représentant le bibliothécaire, responsable de la gestion des documents et des membres."""
    def __init__(self):
        self._catalogue = []
        self._membres = {}

    def ajouter_document(self, document):
        """Ajoute un document au catalogue."""
        self._catalogue.append(document)

    def inscrire_membre(self, nom):
        """Inscrit un nouveau membre à la bibliothèque."""
        if nom in self._membres:
            raise Exception("Membre déjà inscrit.")
        self._membres[nom] = []

    def trouver_document(self, titre):
        """Recherche un document dans le catalogue par son titre."""
        for doc in self._catalogue:
            if doc.titre == titre:
                return doc
        return None

    def emprunter_document(self, titre, nom):
        """Permet à un membre d'emprunter un document s'il est disponible."""
        if nom not in self._membres:
            raise Exception("Membre introuvable.")

        # Recherche du document dans le catalogue
        doc = self.trouver_document(titre)

        if not doc:
            raise Exception("Document introuvable.")

        doc.emprunter()  # polymorphisme
        self._membres[nom].append(doc)


    def retourner_document(self, titre, nom):
        """Permet à un membre de retourner un document emprunté."""
        if nom not in self._membres:
            raise Exception("Membre introuvable.")

        # Recherche du document dans le catalogue
        doc = self.trouver_document(titre)

        # Vérifie que le membre a bien emprunté ce document
        if doc in self._membres[nom]:
            doc.retourner()
            self._membres[nom].remove(doc) # on retire le document de la liste des emprunts du membre
        else:
            raise Exception("Ce membre n'a pas emprunté ce document.")

    def afficher_catalogue(self):
        """Affiche le catalogue de la bibliothèque."""
        return self._catalogue

    def afficher_membres(self):
        """Affiche la liste des membres et leurs emprunts."""
        return self._membres


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