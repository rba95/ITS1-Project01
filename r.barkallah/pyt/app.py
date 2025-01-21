import socket
from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from werkzeug.security import check_password_hash

# Créer une instance de l'application Flask
app = Flask(__name__, static_folder='site', template_folder='site/html')

# Clé secrète pour la gestion des sessions (doit être sécurisée)
app.secret_key = 'supersecretkey'  # Assurez-vous d'utiliser une clé secrète plus complexe et sécurisée

# Connexion à la base de données PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="episen_its",  # Remplace par ton nom de base de données
        user="administrateur",  # Remplace par ton utilisateur PostgreSQL
        password="liberte2024@vitry",  # Remplace par ton mot de passe PostgreSQL
        host="localhost",  # Par défaut, PostgreSQL est en local
        port="5432"
    )
    return conn

# Route pour la page de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Si l'utilisateur est déjà connecté, rediriger vers la page d'accueil
    if 'username' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connexion à la base de données
        conn = get_db_connection()
        cursor = conn.cursor()

        # Vérifier si l'utilisateur existe dans la table etudiant
        cursor.execute("SELECT * FROM etudiant WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user:
            # Vérifier si le mot de passe est correct
            if check_password_hash(user[9], password):  # Le mot de passe est en position 9 dans l'exemple de la table
                # Enregistrer l'utilisateur dans la session
                session['username'] = username
                return redirect(url_for('home'))
            else:
                return "Mot de passe incorrect", 401  # Erreur 401 si le mot de passe est incorrect
        else:
            return "Utilisateur non trouvé", 404  # Erreur 404 si l'username n'est pas trouvé

    return render_template('login.html')  # Affiche le formulaire de login

# Route pour la page d'accueil
@app.route('/')
def home():
    # Vérifier si l'utilisateur est connecté
    if 'username' not in session:
        return redirect(url_for('login'))  # Rediriger vers la page de login si non connecté

    # Afficher la page d'accueil si l'utilisateur est connecté
    return render_template('index.html')

# Route pour se déconnecter
@app.route('/logout')
def logout():
    # Supprimer l'utilisateur de la session
    session.pop('username', None)
    return redirect(url_for('login'))  # Rediriger vers la page de login après déconnexion

if __name__ == "__main__":
    app.run(debug=True)  # Seulement pour le mode développement, Gunicorn sera utilisé en production
