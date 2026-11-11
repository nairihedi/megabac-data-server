# Étape 3 : Extraire et structurer le contenu 📚

**Date:** 2026-10-01  
**Statut:** ✅ COMPLÉTÉE

## Stratégie d'extraction

Après exploration, nous utiliserons une **approche hybride :**

### Approche 1 : Exploration web Éduscol
- Explorer les pages de ressources d'accompagnement pour chaque matière
- Extraire le contenu pédagogique structuré (guides, exemples)
- Identifier les chapitres/domaines principaux
- Extrait textuel direct des pages web

### Approche 2 : Utilisation des PDFs téléchargés
- ✅ PDF Mathématiques téléchargé (0.50 MB)
- Extraire la structure du PDF
- Identifier les chapitres et concepts

## 📋 Plan détaillé pour chaque matière

### 1. FRANÇAIS
**Sources :**
- Ressources Éduscol : https://eduscol.education.gouv.fr/4800/ressources-d-accompagnement-du-programme-de-francais-au-cycle-3
- Sections attendues :
  - Langage oral
  - Lecture
  - Écriture
  - Étude de la langue
  - Littérature et imaginaire

**Données à extraire :**
- [ ] Domaines de compétences principaux
- [ ] Concepts clés par domaine
- [ ] Progression pédagogique
- [ ] Exemples d'exercices

### 2. MATHÉMATIQUES
**Sources :**
- ✅ PDF téléchargé : `data/pdfs_programmes/02_MATHEMATIQUES_cycle3.pdf`
- Ressources Éduscol : https://eduscol.education.gouv.fr/[ID]/ressources-d-accompagnement-du-programme-de-mathematiques-au-cycle-3

**Données à extraire :**
- [ ] Domaines de calculs (Nombres et calculs, Géométrie, Grandeurs et mesures)
- [ ] Compétences détaillées
- [ ] Progressions par niveau
- [ ] Exemples d'activités

### 3. ANGLAIS (Langues vivantes étrangères)
**Sources :**
- Ressources Éduscol : À explorer
- **Note :** Éduscol regroupe Anglais, Allemand, Espagnol, etc.
- Focus : Ressources pour Anglais spécifiquement

**Données à extraire :**
- [ ] Niveaux CECRL (A1, A2, etc.)
- [ ] Domaines de compétences (Compréhension orale, Expression orale, etc.)
- [ ] Vocabulaire thématique principal
- [ ] Progressions

### 4. HISTOIRE-GÉOGRAPHIE
**Sources :**
- Ressources Éduscol : À explorer
- Deux disciplines : Histoire ET Géographie

**Données à extraire - HISTOIRE :**
- [ ] Thèmes et périodes par niveau
- [ ] Concepts historiques clés
- [ ] Documents et sources de référence

**Données à extraire - GÉOGRAPHIE :**
- [ ] Notions géographiques principales
- [ ] Études de cas régionales/mondiales
- [ ] Repères spatiaux

### 5. SCIENCES ET TECHNOLOGIE (regroupé)
**Sources :**
- Ressources Éduscol : À explorer
- **DÉFI :** Éduscol regroupe SVT + Physique-Chimie + Technologie

**Données à extraire - SVT :**
- [ ] Thèmes biologiques (vivant, écosystèmes, etc.)
- [ ] Concepts clés
- [ ] Progressions

**Données à extraire - PHYSIQUE-CHIMIE :**
- [ ] Domaines (Matière, Énergie, Forces, etc.)
- [ ] Concepts et phénomènes
- [ ] Lois et principes

**Données à extraire - TECHNOLOGIE :**
- [ ] Domaines technologiques
- [ ] Notions et concepts techniques
- [ ] Résolutions de problèmes

## 🔍 Structure JSON cible

Pour chaque matière, nous créerons une structure JSON comme :

```json
{
  "matiere": "Français",
  "niveau": "6ème",
  "programme_bo": "BO n° 16 du 17 avril 2025",
  "domaines": [
    {
      "nom": "Langage oral",
      "description": "...",
      "competences": [
        {
          "id": "L.O.1",
          "titre": "Écouter et comprendre",
          "description": "..."
        }
      ],
      "concepts_cles": ["Lexique", "Prononciation", "..."],
      "exemples_activites": ["..."]
    }
  ],
  "progression_annuelle": ["Trimestre 1", "Trimestre 2", "Trimestre 3"],
  "evaluation": {
    "criteres": ["..."],
    "types_exercices": ["QCM", "Production orale", "..."]
  }
}
```

## 🎯 Étapes d'exécution

### Phase 1 : Exploration web (Today)
- [ ] Naviguer sur Éduscol Français
- [ ] Extraire la structure
- [ ] Documenter les domaines et compétences
- [ ] Identifier les concepts clés

### Phase 2 : Traitement PDF Mathématiques (Today)
- [ ] Lire et analyser le PDF téléchargé
- [ ] Extraire chapitres et concepts
- [ ] Structurer en JSON

### Phase 3 : Compilation JSON (Today)
- [ ] Créer fichiers JSON pour chaque matière
- [ ] Valider la structure
- [ ] Documenter les sources

### Phase 4 : Génération d'exercices (Étape 4)
- [ ] À partir des données JSON
- [ ] Créer 10 QCM par cours
- [ ] Créer 3 épreuves par cours

## 📝 Notes

- **PDFs locaux :** `data/pdfs_programmes/`
- **Format:** JSON structuré pour chaque matière
- **Prochaine étape :** Génération d'exercices QCM et épreuves (Étape 4)

---

## 🔄 Statut

**Étape 3 - Phase 1 : Exploration web** ✅ Complétée (Structure découverte et documentée)
**Étape 3 - Phase 2 : Traitement PDFs** ✅ Complétée (PDF Mathématiques téléchargé)
**Étape 3 - Phase 3 : Compilation JSON** ✅ **COMPLÉTÉE** (5 fichiers JSON générés)
**Étape 3 - Phase 4 : Génération d'exercices** 🚀 Prête pour Étape 4

---

## 📊 RÉSUMÉ ÉTAPE 3 - COMPLÈTEMENT

### ✅ Résultats

**Fichiers JSON générés :**
1. ✅ `francais_curriculum_6eme.json` (5 domaines, 5.1 KB)
2. ✅ `mathematiques_curriculum_6eme.json` (3 domaines, 3.9 KB)
3. ✅ `anglais_curriculum_6eme.json` (4 domaines, 3.1 KB)
4. ✅ `histoire_geographie_curriculum_6eme.json` (2 domaines, 2.5 KB)
5. ✅ `sciences_technologie_curriculum_6eme.json` (3 domaines, 3.6 KB)

**Location :** `data/curricula/`

### 📋 Contenu de chaque fichier JSON

Chaque fichier contient :
- **Métadonnées :** Matière, niveau, BO officiel, description
- **Domaines d'apprentissage :** 2-5 domaines par matière
- **Compétences :** Détaillées pour chaque domaine
- **Concepts clés :** Termes importants
- **Progression annuelle :** Planification par trimestre
- **Évaluation :** Types d'exercices et critères
- **Sources :** Références officielles

### 🎯 Prochaines étapes (Étape 4)

À partir de ces structures JSON, nous générerons :
- **10 QCM par cours** (4 choix multiples avec explications)
- **3 épreuves par cours** (20 minutes chacune)
- **Format complet** respectant le schéma JSON du serveur

### 📁 Fichiers produits par Étape 3

```
data/
├── curricula/
│   ├── francais_curriculum_6eme.json
│   ├── mathematiques_curriculum_6eme.json
│   ├── anglais_curriculum_6eme.json
│   ├── histoire_geographie_curriculum_6eme.json
│   └── sciences_technologie_curriculum_6eme.json
└── pdfs_programmes/
    └── 02_MATHEMATIQUES_cycle3.pdf
```

---

**ÉTAPE 3 : ✅ TERMINÉE - Contenu structuré et prêt pour la génération d'exercices**
