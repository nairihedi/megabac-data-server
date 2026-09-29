# Megabac Data Server

Données statiques (JSON) pour l'application Megabac.

## Structure

```
exemple-donnees-serveur/
├── 6/                    # Niveau 6ème
│   ├── version.json      # Numéro de version du contenu
│   ├── matieres.json     # Liste des matières
│   ├── cours/            # Cours par matière
│   ├── cours-detail/     # Détail de chaque cours
│   ├── exercices/        # Exercices par matière
│   ├── exercices-detail/ # Détail de chaque exercice
│   ├── epreuves/         # Épreuves par matière
│   ├── epreuves-detail/  # Détail de chaque épreuve
│   └── matieres/         # Versions par matière
├── 5/                    # Niveau 5ème
└── ...                   # Autres niveaux
```

## Déploiement

### Option 1 : Serveur Python simple
```bash
python -m http.server 80 --directory .
```

### Option 2 : Node.js http-server
```bash
npx http-server -p 80
```

### Option 3 : IIS/Apache
Copier l'arborescence dans le docroot

### Option 4 : CDN
S3, Google Cloud Storage, Azure Blob Storage, etc.

## Configuration dans l'app

Dans `www/js/api.js` :
```javascript
STATIC_BASE_URL = 'http://your-server.com/path/to/data'
MODE = 'static'
```

## Format des données

Chaque fichier JSON suit un schéma spécifique :

### Matière (liste)
```json
[
  { "id": "maths", "nom": "Mathématiques", "icone": "📐" }
]
```

### Cours (détail)
```json
{
  "id": "maths-c1",
  "titre": "Titre du cours",
  "contenu": "<h2>Contenu HTML</h2>"
}
```

### Exercice (QCM)
```json
{
  "id": "maths-e1",
  "type": "qcm",
  "question": "La question ?",
  "choix": ["A", "B", "C", "D"],
  "reponseCorrecte": 0,
  "explication": "Pourquoi A est correct"
}
```

### Épreuve (complète)
```json
{
  "id": "maths-ep1",
  "titre": "Titre",
  "dureeMinutes": 120,
  "bareme": 20,
  "questions": [
    { "id": "q1", "type": "qcm", "enonce": "...", ... }
  ]
}
```

## Voir aussi

- [megabac](https://github.com/your-user/megabac) - Application mobile
- [megabac-api-backend](https://github.com/your-user/megabac-api-backend) - Backend API
- [megabac-admin-tool](https://github.com/your-user/megabac-admin-tool) - Outil d'administration
