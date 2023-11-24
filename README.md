# Projet 9 Application web de critiques de livres ou d'articles OpenClassRooms

A la demande de la jeune start-up LITRevu, j'ai realisé ce projet développé avec Django, qui fournit une plateforme permettant à une communauté d'utilisateurs de publier des critiques de livres ou d’articles et de consulter ou de solliciter une critique de livres à la demande.

## Installation

### Prérequis

- Python ≥ 3.10.12
- Django ≥ 4.2.6

### Étapes pour l'installation

1. Clonez le dépôt depuis GitHub :

    ```bash
    git clone https://github.com/loutreceleste/project9OC.git
    ```

2. Accédez au répertoire du projet :

    ```bash
    cd project9OC
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Créez les migrations pour la base de données :

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Créez un super utilisateur pour accéder à l'interface admin :

    ```bash
    python manage.py createsuperuser
    ```

    Suivez les instructions pour définir un nom d'utilisateur et un mot de passe.

## Lancement du serveur local

Pour démarrer le serveur de développement, exécutez la commande suivante :

```bash
python manage.py runserver
```

Le site sera accessible à l'adresse : http://localhost:8000/

## Accéder à l'interface admin
Lancez le serveur local (si ce n'est pas déjà fait).

Accédez à l'interface admin depuis un navigateur web à l'adresse :

http://localhost:8000/admin/

Connectez-vous en utilisant les informations du super utilisateur créé précédemment ou avec l'identifiant fourni ci dessous.

## Informations de test de connexion
- **Identifiant:** admin **Mot de passe:** admin *super utilisateur*
- **Identifiant:** jean **Mot de passe:** jeanjean
- **Identifiant:** marc **Mot de passe:** marcmarc

## Contribuer
Toute contribution est la bienvenue ! N'hésitez pas à ouvrir une pull request ou à signaler des problèmes.

## Auteurs
Edward Peytavin https://github.com/loutreceleste
