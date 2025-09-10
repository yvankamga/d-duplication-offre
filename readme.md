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
{
  "Forts": [
    {
      "cluster_id": 0,
      "ids": [
        "REC0022",
        "REC0023"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 1,
      "ids": [
        "REC0039",
        "REC0040"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 4,
      "ids": [
        "REC0031",
        "REC0032"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 5,
      "ids": [
        "REC0020",
        "REC0021"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 7,
      "ids": [
        "REC0016",
        "REC0017"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 10,
      "ids": [
        "REC0027",
        "REC0028"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 11,
      "ids": [
        "REC0047",
        "REC0048",
        "REC0049"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 12,
      "ids": [
        "REC0018",
        "REC0019"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 13,
      "ids": [
        "REC0037",
        "REC0038"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 14,
      "ids": [
        "REC0024",
        "REC0025"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 15,
      "ids": [
        "REC0029",
        "REC0030"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 18,
      "ids": [
        "REC0043",
        "REC0044"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 23,
      "ids": [
        "REC0045",
        "REC0046"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 24,
      "ids": [
        "REC0035",
        "REC0036"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 26,
      "ids": [
        "REC0041",
        "REC0042"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 30,
      "ids": [
        "REC0033",
        "REC0034"
      ],
      "score_explicatif": "url_match"
    },
    {
      "cluster_id": 3,
      "ids": [
        "REC0003",
        "REC0004",
        "REC0015"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 6,
      "ids": [
        "REC0006",
        "REC0011",
        "REC0013"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 7,
      "ids": [
        "REC0008",
        "REC0009"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 10,
      "ids": [
        "REC0016",
        "REC0017"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 11,
      "ids": [
        "REC0018",
        "REC0019"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 12,
      "ids": [
        "REC0020",
        "REC0021"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 13,
      "ids": [
        "REC0022",
        "REC0023"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 14,
      "ids": [
        "REC0024",
        "REC0025"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 16,
      "ids": [
        "REC0027",
        "REC0028"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 17,
      "ids": [
        "REC0029",
        "REC0030"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 18,
      "ids": [
        "REC0031",
        "REC0032"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 19,
      "ids": [
        "REC0033",
        "REC0034"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 20,
      "ids": [
        "REC0035",
        "REC0036"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 21,
      "ids": [
        "REC0037",
        "REC0038"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 22,
      "ids": [
        "REC0039",
        "REC0040"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 23,
      "ids": [
        "REC0041",
        "REC0042"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 24,
      "ids": [
        "REC0043",
        "REC0044"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 25,
      "ids": [
        "REC0045",
        "REC0046"
      ],
      "score_explicatif": "external_id_match"
    },
    {
      "cluster_id": 26,
      "ids": [
        "REC0047",
        "REC0048",
        "REC0049"
      ],
      "score_explicatif": "external_id_match"
    }
  ],
  "Probables": [
    {
      "cluster_id": 0,
      "ids": [
        "REC0006",
        "REC0008",
        "REC0009",
        "REC0011",
        "REC0013"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 1,
      "ids": [
        "REC0031",
        "REC0032"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 2,
      "ids": [
        "REC0020",
        "REC0021"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 3,
      "ids": [
        "REC0043",
        "REC0044"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 4,
      "ids": [
        "REC0047",
        "REC0048",
        "REC0049"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 5,
      "ids": [
        "REC0041",
        "REC0042"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 6,
      "ids": [
        "REC0039",
        "REC0040"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 7,
      "ids": [
        "REC0029",
        "REC0030"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 8,
      "ids": [
        "REC0033",
        "REC0034"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 9,
      "ids": [
        "REC0024",
        "REC0025"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 10,
      "ids": [
        "REC0022",
        "REC0023"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 11,
      "ids": [
        "REC0027",
        "REC0028"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 12,
      "ids": [
        "REC0016",
        "REC0017"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 15,
      "ids": [
        "REC0035",
        "REC0036"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 17,
      "ids": [
        "REC0005",
        "REC0007"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 19,
      "ids": [
        "REC0018",
        "REC0019"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 20,
      "ids": [
        "REC0037",
        "REC0038"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 22,
      "ids": [
        "REC0045",
        "REC0046"
      ],
      "score_explicatif": "similarité_description≥0.85"
    },
    {
      "cluster_id": 24,
      "ids": [
        "REC0003",
        "REC0004",
        "REC0015"
      ],
      "score_explicatif": "similarité_description≥0.85"
    }
  ]
}
```
