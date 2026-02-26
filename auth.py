import bcrypt
from db import connection_db
import getpass


class Authentification:

    def __init__(self):
        self.actuelle_user = None


    # ================== INSCRIPTION ==================
    def inscription(self):

        connexion = connection_db()
        if not connexion:
            return

        curseur = connexion.cursor()

        try:
            while True:
                nom = input("Entrer votre Nom: ").strip()
                if not nom.isalpha():
                    print("Nom invalide.")
                    continue
                break

            while True:
                email = input("Entrer votre Email: ").strip()
                if not email or "@" not in email:
                    print("Email invalide.")
                    continue
                break

            while True:
                password = getpass.getpass("Entrer votre Mot de passe: ").strip()
                if not password or len(password) < 8:
                    print("Mot de passe invalide (minimum 8 caractères).")
                    continue
                break

            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

            curseur.execute("""
                INSERT INTO utilisateurs (nom, email, mot_de_passe)
                VALUES (%s, %s, %s)
            """, (nom, email, hashed_password.decode()))

            connexion.commit()
            print("Compte créé avec succès.")

        except Exception as e:
            print("Erreur :", e)

        finally:
            connexion.close()


    # ================== CONNEXION ==================
    def connexion(self):

        connexion = connection_db()
        if not connexion:
            return

        curseur = connexion.cursor(dictionary=True)

        try:
            while True:
                email = input("Entrer votre Email: ").strip()
                if not email or "@" not in email:
                    print("Email invalide.")
                    continue
                break

            while True:
                password = getpass.getpass("Entrer votre Mot de passe: ").strip()
                if not password:
                    print("Mot de passe invalide.")
                    continue
                break

            curseur.execute("SELECT * FROM utilisateurs WHERE email = %s", (email,))
            user = curseur.fetchone()

            if user and bcrypt.checkpw(password.encode(), user['mot_de_passe'].encode()):
                self.actuelle_user = user
                print("Connexion réussie.")
            else:
                print("Identifiants incorrects.")

        except Exception as e:
            print("Erreur :", e)

        finally:
            connexion.close()


    # ================== DECONNEXION ==================
    def deconnexion(self):
        self.actuelle_user = None
        print("Déconnexion réussie.")
    