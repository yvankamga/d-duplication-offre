# Cas 2 — Outil de déduplication d’offres multi-sources (Python)

## Objectif

Ce projet vise à développer un outil de déduplication d’offres multi-sources. l'outil devra permettre de trouver les offres dupliquées dans un fichier CSV contenant des offres d'emplois provenant de plusieurs sources.

## Comment lancer l'outil

- Modifier le fichier data.csv avec les offres d'emplois que vous souhaitez dédupliquer

- Créer un environnement virtuel
```bash
python3 -m venv venv
```

- Activer l'environnement virtuel
```bash
source venv/bin/activate
```

- installer les dépendances
```bash
pip3 install -r requirements.txt
```

- lancer l'outil
```bash
python3 main.py
```

Vous pouvez trouver le résultat dans le fichier result.json

## Fonctionnement

- L'outil utilise plusieurs méthodes pour trouver les offres dupliquées :
    - urlMatch : compare les urls des offres (supprime les paramètres de la url, les tags, les paramètres de la requête, http/https)
    - keyCanonica : compare les titre+entreprise+ville+date des offres
    - externalIdMatch : compare les id externes des offres
    - similarilyMatch : compare les descriptions des offres

- L'outil utilise un algorithme de clustering pour trouver les offres dupliquées
    - tf-idf : permet de calculer la similarité entre les descriptions des offres
    - utilisaation de pandas pour gérer les données et les regrouper en clusters


## Exemple de résultat

En lançant l'outil sur le fichier data.csv, vous pouvez trouver le résultat dans le fichier result.json

```json

