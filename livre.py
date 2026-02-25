from document import Document


class Livre(Document):
    """Classe représentant un livre."""

    def __init__(self, titre, auteur, disponible=True, doc_id=None):
        super().__init__(titre, "livre", disponible, doc_id)
        self._auteur = auteur

    @property
    def auteur(self):
        return self._auteur

    def emprunter(self):
        if not self.disponible:
            raise Exception("Livre déjà indisponible.")
        self._changer_disponibilite(False)

    def retourner(self):
        self._changer_disponibilite(True)

    def __str__(self):
        statut = "Disponible" if self.disponible else "Indisponible"
        return f"Livre: {self.titre} | Auteur: {self.auteur} | {statut}"