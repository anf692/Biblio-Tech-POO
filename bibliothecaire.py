from livre import Livre
from magazine import Magazine
from db import connection_db
from datetime import datetime



class Bibliothecaire:
    """Classe représentant un bibliothécaire qui gère les opérations de la bibliothèque."""

    def ajouter_document(self, document):
        """Ajoute un nouveau document (livre ou magazine) à la bibliothèque."""

        conn=connection_db()
        cursor = conn.cursor()

        # insertion dans documents
        sql_doc = """
        INSERT INTO documents (titre, type_doc, disponible)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql_doc, (document.titre, document.type_doc, document.disponible))

        # récupérer id généré
        doc_id = cursor.lastrowid

        # insertion dans table spécifique
        if document.type_doc == "livre":
            cursor.execute(
                "INSERT INTO livres (document_id, auteur) VALUES (%s,%s)",
                (doc_id, document.auteur)
            )
        else:
            cursor.execute(
                "INSERT INTO magazines (document_id, numero) VALUES (%s,%s)",
                (doc_id, document.numero)
            )

        conn.commit()
        cursor.close()
        conn.close()


    def inscrire_membre(self, nom):
        """Inscrit un nouveau membre à la bibliothèque."""
        conn=connection_db()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO membres (nom) VALUES (%s)", (nom,))

        conn.commit()
        cursor.close()
        conn.close()

    
    def trouver_document(self, titre):
        """Recherche un document par son titre et le retourne sous forme d'objet Livre ou Magazine."""

        conn=connection_db()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM documents WHERE titre=%s or id=%s", (titre, titre))

        # récupérer données document
        doc = cursor.fetchone()

        # si pas trouvé
        if not doc:
            return None

        # construire objet selon type
        if doc["type_doc"] == "livre":
            cursor.execute("SELECT auteur FROM livres WHERE document_id=%s", (doc["id"],))

            # récupérer auteur
            auteur = cursor.fetchone()["auteur"]

            # créer objet Livre
            document = Livre(doc["titre"], doc["type_doc"], auteur)

        else:
            cursor.execute("SELECT numero FROM magazines WHERE document_id=%s", (doc["id"],))

            # récupérer numéro
            numero = cursor.fetchone()["numero"]

            # créer objet Magazine
            document = Magazine(doc["titre"], doc["type_doc"], numero)

        # mettre à jour disponibilité
        if not doc["disponible"]:
            document._changer_disponibilite(False)

        cursor.close()
        conn.close()

        return document
    

    def emprunter_document(self, titre, nom):
        """Permet à un membre d'emprunter un document s'il est disponible."""
        conn=connection_db()
        cursor = conn.cursor(dictionary=True)

        # récupérer document
        cursor.execute("SELECT * FROM documents WHERE titre=%s", (titre,))
        
        # récupérer données document
        doc = cursor.fetchone()

        # vérifier existence et disponibilité
        if not doc:
            raise Exception("Document introuvable.")

        # vérifier disponibilité
        if not doc["disponible"]:
            raise Exception("Document déjà emprunté.")

        # récupérer membre
        cursor.execute("SELECT * FROM membres WHERE nom=%s", (nom,))
        # récupérer données membre
        membre = cursor.fetchone()

        # vérifier existence membre
        if not membre:
            raise Exception("Membre introuvable.")

        # mise à jour disponibilité
        cursor.execute(
            "UPDATE documents SET disponible=FALSE WHERE id=%s",
            (doc["id"],)
        )

        # insertion emprunt
        cursor.execute(
            "INSERT INTO emprunts (membre_id, document_id) VALUES (%s,%s)",
            (membre["id_membre"], doc["id"])
        )

        conn.commit()
        cursor.close()
        conn.close()

    
    def retourner_document(self, titre, nom):
        """Permet à un membre de retourner un document emprunté."""
        conn=connection_db()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM documents WHERE titre=%s", (titre,))
        # récupérer données document
        doc = cursor.fetchone()

        # récupérer membre
        cursor.execute("SELECT * FROM membres WHERE nom=%s", (nom,))
        # récupérer données membre
        membre = cursor.fetchone()

        # vérifier existence document et membre
        if not doc or not membre:
            raise Exception("Erreur données incorrect.")

        # vérifier emprunt actif
        cursor.execute("""
            SELECT * FROM emprunts
            WHERE membre_id=%s AND document_id=%s AND date_retour IS NULL
        """, (membre["id_membre"], doc["id"]))

        # récupérer emprunt actif
        emprunt = cursor.fetchone()

        if not emprunt:
            raise Exception("Ce membre n'a pas emprunté ce document.")


        # rendre disponible
        cursor.execute(
            "UPDATE documents SET disponible=TRUE WHERE id=%s",
            (doc["id"],)
        )

        # marquer retour
        cursor.execute("""
            UPDATE emprunts
            SET date_retour=%s
            WHERE id=%s
        """, (datetime.now(), emprunt["id"]))

        conn.commit()
        cursor.close()
        conn.close()


    def afficher_catalogue(self):
        """Affiche tous les documents de la bibliothèque avec leur statut de disponibilité."""
        conn=connection_db()
        cursor = conn.cursor(dictionary=True)

        catalogue = []

        cursor.execute("""
            SELECT d.id, d.titre, d.disponible, l.auteur
            FROM documents d
            JOIN livres l ON d.id = l.document_id
            WHERE d.type_doc = 'livre'
        """)
        livres = cursor.fetchall()

        for doc in livres:
            document = Livre(doc["titre"],doc["auteur"],doc["disponible"],doc["id"])
            catalogue.append(document)

       
        cursor.execute("""
            SELECT d.id, d.titre, d.disponible, m.numero
            FROM documents d
            JOIN magazines m ON d.id = m.document_id
            WHERE d.type_doc = 'magazine'
        """)
        magazines = cursor.fetchall()

        for doc in magazines:
            document = Magazine(doc["titre"],doc["numero"], doc["disponible"],doc["id"])

            catalogue.append(document)

        cursor.close()
        conn.close()

        return catalogue
    

    def afficher_membres(self):
        """Affiche tous les membres inscrits à la bibliothèque."""
        conn=connection_db()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM membres")
        membres = cursor.fetchall()

        result = {}

        for membre in membres:
            cursor.execute("""
                SELECT d.titre, d.type_doc, d.disponible, l.auteur, m.numero
                FROM emprunts e
                JOIN documents d ON e.document_id=d.id
                LEFT JOIN livres l ON d.id=l.document_id
                LEFT JOIN magazines m ON d.id=m.document_id
                WHERE e.membre_id=%s AND e.date_retour IS NULL
            """, (membre["id_membre"],))

            emprunts = cursor.fetchall()

            emprunt_docs = []

            for emprunt in emprunts:
                if emprunt["type_doc"] == "livre":
                    doc = Livre(emprunt["titre"], emprunt["type_doc"], emprunt["auteur"])
                else:
                    doc = Magazine(emprunt["titre"], emprunt["type_doc"], emprunt["numero"])

                if not emprunt["disponible"]:
                    doc._changer_disponibilite(False)

                emprunt_docs.append(doc)

            result[membre["nom"]] = emprunt_docs

        cursor.close()
        conn.close()

        return result
        
        
    def afficher_emprunts_membre(self, nom):
        """Affiche tous les documents empruntés par un membre donné."""
        conn=connection_db()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM membres WHERE nom=%s", (nom,))
        membre = cursor.fetchone()

        if not membre:
            raise Exception("Membre introuvable.")

        cursor.execute("""
            SELECT d.titre, d.type_doc, d.disponible, l.auteur, m.numero
            FROM emprunts e
            JOIN documents d ON e.document_id=d.id
            LEFT JOIN livres l ON d.id=l.document_id
            LEFT JOIN magazines m ON d.id=m.document_id
            WHERE e.membre_id=%s AND e.date_retour IS NULL
        """, (membre["id_membre"],))

        emprunts = cursor.fetchall()

        result = []

        for emprunt in emprunts:
            if emprunt["type_doc"] == "livre":
                doc = Livre(emprunt["titre"], emprunt["type_doc"], emprunt["auteur"])
            else:
                doc = Magazine(emprunt["titre"], emprunt["type_doc"], emprunt["numero"])

            if not emprunt["disponible"]:
                doc._changer_disponibilite(False)

            result.append(doc)

        cursor.close()
        conn.close()

        return result



