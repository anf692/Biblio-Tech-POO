from document import Document

class Magazine(Document):
    """Classe représentant un magazine, héritant de Document."""
    def __init__(self, titre, type_doc, numero):
        super().__init__(titre, type_doc)
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
