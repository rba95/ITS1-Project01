import psycopg2
from werkzeug.security import generate_password_hash

# Connexion à la base de données PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="episen_its",  # Remplace par le nom de ta base de données
        user="administrateur",  # Remplace par ton utilisateur PostgreSQL
        password="liberte2024@vitry",  # Remplace par ton mot de passe PostgreSQL
        host="localhost",  # Par défaut, PostgreSQL est en local
        port="5432"
    )
    return conn

# Fonction pour hacher les mots de passe
def hash_passwords():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Récupérer tous les utilisateurs
    cursor.execute("SELECT etudiant_id, password FROM etudiant")
    users = cursor.fetchall()

    for user in users:
        etudiant_id, password = user
        # Hacher le mot de passe
        hashed_password = generate_password_hash(password)

        # Mettre à jour le mot de passe dans la base de données
        cursor.execute(
            "UPDATE etudiant SET password = %s WHERE etudiant_id = %s",
            (hashed_password, etudiant_id)
        )
        print(f"Mot de passe de l'utilisateur {etudiant_id} mis à jour.")

    # Commit les modifications et fermer la connexion
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    hash_passwords()
