Medima-API
==========

Ce projet vise à créer une API REST pour le site
web https://medicament.ma. Il possède un script qui
utilise l'api pour récupérer des informations de
base sur les médicaments.


Endpoints disponibles
---------------------

* /search/
    Rechercher un médicament suivant divers paramètres:

    * *q*: le texte de la recherche (obligatoire. exple: doliprane)
        La signification de ce texte dépend de la valeur du paramètre **c**

    * *c*: type de classification de la recherche (obligatoire)
        Valeurs possibles:

        * *specialite*: recherche par nom commercial
        * *dci*: recherche par substance active
        * *price*: recherche par prix
        * *fournisseur*: recherche par fournisseur
        * *barcode*: recherche par le code barre

    * *k*: règle de recherche (obligatoire pour les classifications de type **specialite** et **dci**)
        Valeurs possible: *contains* et *starts*

* /detail/{abrégé-du-medoc}
    Obtenir des métadonnées supplémentaire d'un médicament. **{abrégé-du-medoc}** est
    obtenu en faisant une requête de recherche dans un premier temps (clé *slug*) dans
    le résultat de recherche.


Installation
____________


* Installer Python 3 (à partir de 3.3, en montant)
* Installer git
* Cloner le dépôt: `git clone https://github.com/aoyono/medima.git`
* Naviguer vers le dépôt local: `cd medima`
* Créer un environnement virtuel: `python -m venv env-medima`
* Activer l'environnement virtuel:
    * Linux: `source env-medima/bin/activate`
    * windows: `env-medima\Scripts\activate.bat` ou `env-medima\Scripts\Activate.ps1`
* Installer les dépendances: `python -m pip install -r requirements.txt`


Utilisation
-----------

* Lancer uniquement le serveur:
    `python app.py`

* Effectuer une recherche (lance le serveur, effectue la recherche et stoppe le serveur):
    `python __main__.py {q} {c} {k}`


Dépendances
-----------

* Requests: https://github.com/requests/requests (License Apache 2.0)
* Toapi: https://github.com/gaojiuli/toapi (License Apache 2.0)


License
-------

GPLv3