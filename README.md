# ARConnect-Manager 


ARConnect-Manager is a webapp created to manage tournaments in a LAN-like event. 

[Access the demo here](https://arconnect.k8s.ing.he-arc.ch/)

### Installation du projet en local
1. Cloner le projet en local
2. Installer les modules pythons qui sont dans `./Api/requirements.txt`
3. Dans `./Api/.`, lancer les migrations avec la ocmmande `python manage.py migrate`
4. Toujours au même endroit, exécuter le serveur avec la commande `python manage.py runserver`
5. Se déplacer dans `./frontend/`
6. Installer les modules NPM avec la commande `npm install`
7. Démarrer le serveur avec la commande `npm run dev`

### Sources 

- [allauth](https://docs.allauth.org/en/latest/)
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/index.html)
- [api challonge](https://api.challonge.com/v1)
- [module python api challonge](https://github.com/ZEDGR/pychallonge)
