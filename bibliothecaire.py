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



