from document import Document


class Magazine(Document):
    """Classe représentant un magazine."""

    def __init__(self, titre, numero, disponible=True, doc_id=None):
        super().__init__(titre, "magazine", disponible, doc_id)
        self._numero = numero

    @property
    def numero(self):
        return self._numero

    def emprunter(self):
        if not self.disponible:
            raise Exception("Magazine déjà indisponible.")
        self._changer_disponibilite(False)

    def retourner(self):
        self._changer_disponibilite(True)

    def __str__(self):
        statut = "Disponible" if self.disponible else "Indisponible"
        return f"Magazine: {self.titre} | Numéro: {self.numero} | {statut}"