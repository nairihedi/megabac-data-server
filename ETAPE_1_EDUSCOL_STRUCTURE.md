# Étape 1 : Découvrir la structure d'Éduscol ✅

**Date:** 2026-10-01  
**Statut:** Complétée

## Résumé de l'exploration

Site exploré : https://eduscol.education.gouv.fr/

### 1️⃣ Navigation générale

L'accueil d'Éduscol propose 3 menus principaux :
- **Enseignement et formation** → Niveaux, Disciplines, Pratique enseignante, Thématiques
- **Scolarité de l'élève et diplômes**
- **Vie des écoles et des établissements**

### 2️⃣ Organisation par niveaux

Éduscol utilise une classification par **Cycles** :
- **Cycle 1** : Maternelle
- **Cycle 2** : CP, CE1, CE2
- **Cycle 3** : CM1, CM2, 6ème ← **Notre focus initial**
- **Cycle 4** : 5ème, 4ème, 3ème
- **Lycée** : 2nde, 1ère, Terminale (général/technologique et professionnel)

### 3️⃣ Disciplines disponibles pour la 6ème (Cycle 3)

Pour la classe de 6ème, Éduscol propose ces 8 disciplines :

| # | Discipline | BO officiel | Statut |
|---|---|---|---|
| 1 | Français | BO n° 16 du 17 avril 2025 | Mis à jour 2025 |
| 2 | Mathématiques | BO n° 16 du 17 avril 2025 | Mis à jour 2025 |
| 3 | Histoire-géographie | BO n° 31 du 30 juillet 2020 | En vigueur |
| 4 | Langues vivantes étrangères | BO n° 22 du 29 mai 2025 | Mis à jour 2025 |
| 5 | Langues vivantes régionales | BO n° 21 du 21 mai 2026 | NOUVEAU 2026 |
| 6 | Sciences et technologie | BO n° 25 du 22 juin 2023 | En vigueur |
| 7 | Enseignements artistiques | BO n° 31 du 30 juillet 2020 | (Arts plastiques, Musique, Histoire des arts) |
| 8 | Enseignement moral et civique | BO n° 24 du 13 juin 2024 | NOUVEAU 2024 |
| 9 | Éducation physique et sportive | BO n° 31 du 30 juillet 2020 | En vigueur |
| 10 | Education à la vie affective et relationnelle | BO n° 6 du 6 février 2025 | Mis à jour 2025 |

**Note :** Certains sujets ne correspondent pas exactement aux 6 matières Megabac (Français, Maths, Anglais, SVT, Physique-Chimie, Histoire-Géographie).
- **Sciences et technologie** (Éduscol) ≠ SVT + Physique-Chimie (Megabac)
- **Langues vivantes** = Anglais principalement
- Disciplines complémentaires sur Éduscol : Enseignements artistiques, Moral/civique, Vie affective

### 4️⃣ Types de ressources fournies

Pour chaque discipline, Éduscol fournit :

#### A. Programmes officiels (PDF)
- **Fichiers PDF téléchargeables** : Les programmes complets au format PDF
- **Exemple** : `programme-de-fran-ais-pour-le-cycle-3-439824.pdf`
- **URL pattern** : https://www.education.gouv.fr/sites/default/files/`[nom-fichier].pdf`
- **Contenu** : Référentiel officiel avec compétences, objectifs, progressions

#### B. Ressources d'accompagnement
Trois catégories identifiées :

1. **Les guides fondamentaux**
   - Ressources générales d'accompagnement
   - Guides pour tous les niveaux

2. **Ressources d'accompagnement par discipline**
   - Exemple vus : Ressources pour Français, Ressources pour Mathématiques
   - Contiennent : Pistes pédagogiques, outils, exemples

3. **Évaluations nationales**
   - Tests standardisés par niveau

### 5️⃣ Structure générale découverte

```
Éduscol
├── Accueil
├── Enseignement et formation
│   ├── Cycle 3
│   │   ├── Programmes en application (pour CM1, CM2, 6ème)
│   │   │   ├── Français
│   │   │   ├── Mathématiques
│   │   │   ├── Histoire-géographie
│   │   │   ├── Langues vivantes
│   │   │   ├── Sciences et technologie
│   │   │   ├── Enseignements artistiques
│   │   │   ├── Enseignement moral et civique
│   │   │   ├── Éducation physique et sportive
│   │   │   └── Éducation à la vie affective
│   │   └── Ressources d'accompagnement
│   │       ├── Les guides fondamentaux
│   │       ├── Ressources par discipline (Français, Maths, etc.)
│   │       └── Évaluations nationales
│   ├── Cycle 4 (5ème-3ème)
│   └── Lycée
├── Autres menus...
```

## 📊 Matrice : Éduscol vs Megabac

| Éduscol (6ème/Cycle 3) | Megabac | Correspondance |
|---|---|---|
| Français | Français | ✅ Directe |
| Mathématiques | Mathématiques | ✅ Directe |
| Langues vivantes étrangères | Anglais | ✅ Partiellement (LVE = anglais + autres) |
| Sciences et technologie | SVT + Physique-Chimie | ⚠️ À découpler |
| Histoire-géographie | Histoire-Géographie | ✅ Directe |
| Enseignements artistiques | ❌ Pas dans Megabac | 🚫 Hors scope |
| Enseignement moral et civique | ❌ Pas dans Megabac | 🚫 Hors scope |
| Éducation physique et sportive | ❌ Pas dans Megabac | 🚫 Hors scope |
| Éducation à la vie affective | ❌ Pas dans Megabac | 🚫 Hors scope |

## 🎯 Points clés

1. **Éduscol est bien structuré et organisé** par niveaux et disciplines
2. **Ressources officielles** = Programme PDF + Guides d'accompagnement
3. **Couverture partielle** : Éduscol a toutes les matières Megabac + d'autres hors-scope
4. **Accessibilité** : PDFs directement téléchargeables
5. **Mise à jour régulière** : Programmes mis à jour 2025-2026

## ✅ Étape 1 complétée

Structure découverte et documentée. Prêt pour **Étape 2** : Mapper les documents disponibles et télécharger les PDFs pour 6ème.

---

## 🔗 URLs de référence

- **Accueil Éduscol** : https://eduscol.education.gouv.fr/
- **Cycle 3** : https://eduscol.education.gouv.fr/4356/enseigner-au-cycle-3
- **PDFs Gouvernement** : https://www.education.gouv.fr/sites/default/files/

## 📝 Prochaines étapes

- **Étape 2** : Lister tous les PDFs/guides disponibles pour 6ème (créer matrice complète)
- **Étape 3** : Télécharger et extraire les programmes en PDF
- **Étape 4** : Structurer le contenu en JSON
- **Étape 5** : Générer QCMs et épreuves
