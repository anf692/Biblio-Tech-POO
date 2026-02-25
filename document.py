from abc import ABC, abstractmethod


class Document(ABC):
    """Classe abstraite représentant un document."""

    def __init__(self, titre, type_doc, disponible=True, doc_id=None):
        self._id = doc_id
        self._titre = titre
        self._type_doc = type_doc
        self.__disponible = disponible 

    @property
    def id(self):
        return self._id

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
        pass

    @abstractmethod
    def retourner(self):
        pass

    def _changer_disponibilite(self, etat):
        self.__disponible = etat