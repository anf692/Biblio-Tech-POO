from document import Document

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

