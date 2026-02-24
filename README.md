# 📚 Système de Gestion de Bibliotheque (POO Python)

## Description

Ce projet est une application console développée en **Python** utilisant les principes avancés de la **Programmation Orientée Objet (POO)**.

Il permet de gérer une médiathèque capable de manipuler plusieurs types de supports (Livres, Magazines) de manière évolutive, sécurisée et industrielle.

L'objectif principal est de démontrer :

- L'**abstraction**
- L'**encapsulation**
- Le **polymorphisme**
- Le respect du principe **Open/Closed**
- Une architecture propre et extensible

---


### `Document` (Classe Abstraite)
- Définit la structure commune obligatoire.
- Empêche l'instanciation directe.
- Contient les méthodes abstraites :
  - `emprunter()`
  - `retourner()`
- Protège l'état de disponibilité.

### `Livre`
- Hérite de `Document`
- Possède un attribut spécifique : `auteur`

### `Magazine`
- Hérite de `Document`
- Possède un attribut spécifique : `numero`

### `Bibliothecaire`
- Gère le catalogue
- Gère les membres
- Applique le polymorphisme
- Recherche uniquement par titre

### `Application`
- Interface console
- Menu interactif avec `match/case`

---

## Sécurité & Encapsulation

L'état de disponibilité d’un document :

- N’est pas modifiable directement
- Accessible uniquement en lecture via une propriété
- Modifiable uniquement via les méthodes internes `emprunter()` et `retourner()`

Toute tentative de modification externe provoque une erreur.

---

## Fonctionnalités

- Ajouter un Livre
- Ajouter un Magazine
- Inscrire un membre
- Emprunter un document
- Retourner un document
- Afficher le catalogue
- Lister les emprunts d’un membre
- Démonstration du verrouillage des données

---

## Concepts POO Appliqués

| Concept | Implémentation |
|----------|---------------|
| Abstraction | Classe `Document` abstraite |
| Encapsulation | Attribut privé `__disponible` |
| Polymorphisme | `emprunter()` et `retourner()` |
| Open/Closed Principle | Ajout de nouveaux supports sans modifier `Bibliothecaire` |

---

## Exemple d'utilisation
===== MENU =====
1. Ajouter un Livre
2. Ajouter un Magazine
3. Inscrire un membre
4. Emprunter un document
5. Retourner un document
...

---

## Installation & Exécution

### Cloner le projet

```bash
git clone https://github.com/anf692/Biblio-Tech-POO.git
