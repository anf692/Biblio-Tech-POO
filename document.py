from abc import ABC, abstractmethod

class Document(ABC):
    """Classe abstraite représentant un document de la bibliothèque."""

    def __init__(self, titre, type_doc):
        self._titre = titre
        self._type_doc = type_doc
        self.__disponible = True #(name mangling)

    @property
    def titre(self):
        return self._titre

    @property
    def type_doc(self):
        return self._type_doc

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
