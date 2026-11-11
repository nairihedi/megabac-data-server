#!/usr/bin/env python3
"""
Génération du contenu réel des cours
Étape 3b: Créer les leçons avec le contenu pédagogique
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("./data/courses")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

COURSES_DATA = {
    "francais": {
        "matiere": "Français",
        "niveau": "6ème",
        "courses": [
            {
                "id": "FR_001",
                "titre": "Les parties du discours - Le verbe",
                "domaine": "Étude de la langue",
                "objectifs": [
                    "Identifier un verbe dans une phrase",
                    "Comprendre le rôle du verbe",
                    "Conjuguer les verbes au présent"
                ],
                "contenu": """
## Qu'est-ce qu'un verbe?

Un verbe est un mot qui exprime une **action** ou un **état**.

### Exemples d'actions:
- courir, manger, lire, écrire, danser, sauter

### Exemples d'états:
- être, sembler, paraître, rester, devenir

## Le rôle du verbe dans la phrase

Le verbe est le centre de la phrase. Tous les autres mots gravitent autour du verbe.

### Exemple:
"**Le chat dort** sur le tapis."
- Verbe: "dort" (action que fait le chat)
- Sujet: "Le chat" (qui fait l'action)
- Complément: "sur le tapis" (où il dort)

## Conjugaison au présent (être et avoir)

### Être (présent):
- Je suis
- Tu es
- Il/Elle est
- Nous sommes
- Vous êtes
- Ils/Elles sont

### Avoir (présent):
- J'ai
- Tu as
- Il/Elle a
- Nous avons
- Vous avez
- Ils/Elles ont
""",
                "concepts_cles": {
                    "Verbe": "Mot qui exprime une action ou un état",
                    "Action": "Ce que fait le sujet (courir, manger, lire)",
                    "État": "La situation du sujet (être, sembler, rester)",
                    "Conjugaison": "Modification du verbe selon le sujet"
                },
                "exercices_exemples": [
                    "Identifiez le verbe dans: 'Marie écrit une lettre.'",
                    "Complétez: 'Je ____ heureux.' (être)",
                    "Conjuguez 'avoir' à la 1ère personne du pluriel"
                ]
            },
            {
                "id": "FR_002",
                "titre": "Comprendre une phrase simple",
                "domaine": "Lecture",
                "objectifs": [
                    "Identifier le sujet, verbe et complément",
                    "Comprendre la structure d'une phrase",
                    "Poser les bonnes questions pour analyser"
                ],
                "contenu": """
## Les trois éléments d'une phrase simple

Une phrase simple contient toujours trois éléments principaux:

### 1. Le sujet: QUI fait l'action?
- "**Le chat** dort" → sujet: Le chat

### 2. Le verbe: QUEL est l'action?
- "Le chat **dort**" → verbe: dort

### 3. Le complément: OÙ? QUAND? COMMENT? QUOI?
- "Le chat dort **sur le tapis**" → complément: sur le tapis

## Exemple complet d'analyse:

Phrase: "Les enfants jouent au parc."

- Sujet: "Les enfants" (QUI?)
- Verbe: "jouent" (QUOI? QUELLES ACTION?)
- Complément: "au parc" (OÙ?)

## Les types de questions pour analyser

Pour bien analyser une phrase, posez-vous ces questions:
- QUI? → Sujet
- FAIT QUOI? → Verbe
- OÙ? → Complément de lieu
- QUAND? → Complément de temps
- COMMENT? → Complément de manière
""",
                "concepts_cles": {
                    "Phrase simple": "Une phrase avec un sujet, un verbe et un complément",
                    "Sujet": "La personne ou la chose qui fait l'action",
                    "Verbe": "L'action ou l'état du sujet",
                    "Complément": "Information supplémentaire (lieu, temps, manière)"
                },
                "exercices_exemples": [
                    "Identifiez sujet/verbe/complément dans: 'Sophie lit un livre à la maison.'",
                    "Posez les bonnes questions pour analyser une phrase"
                ]
            }
        ]
    },

    "mathematiques": {
        "matiere": "Mathématiques",
        "niveau": "6ème",
        "courses": [
            {
                "id": "MATH_001",
                "titre": "Les nombres décimaux",
                "domaine": "Nombres et Calculs",
                "objectifs": [
                    "Comprendre la structure des nombres décimaux",
                    "Lire et écrire les nombres décimaux",
                    "Comparer des nombres décimaux"
                ],
                "contenu": """
## Qu'est-ce qu'un nombre décimal?

Un nombre décimal est un nombre qui possède deux parties:
- Une **partie entière** (avant la virgule)
- Une **partie décimale** (après la virgule)

### Exemple:
```
    12,5
    ↑  ↑
  partie partie
  entière décimale
```

## Les chiffres après la virgule

Chaque chiffre après la virgule représente une fraction:
- 1er chiffre = dixièmes (1/10)
- 2e chiffre = centièmes (1/100)
- 3e chiffre = millièmes (1/1000)

### Exemple: 3,456
- 3 = trois unités
- 4 = quatre dixièmes
- 5 = cinq centièmes
- 6 = six millièmes

## Lire un nombre décimal

12,5 se lit: "douze virgule cinq" ou "douze et cinq dixièmes"

## Comparer des nombres décimaux

Pour comparer deux nombres décimaux, on compare d'abord la partie entière:
- 12,5 > 11,8 (car 12 > 11)
- 5,3 < 5,8 (car 5 = 5, mais 3 < 8)

### La règle:
1. Comparer la partie entière
2. Si elle est égale, comparer la première décimale
3. Si elle est égale, comparer la deuxième décimale, etc.
""",
                "concepts_cles": {
                    "Nombre décimal": "Nombre avec une partie entière et décimale",
                    "Virgule": "Séparateur entre la partie entière et décimale",
                    "Dixième": "1/10 = 0,1",
                    "Centième": "1/100 = 0,01",
                    "Millième": "1/1000 = 0,001"
                },
                "exercices_exemples": [
                    "Écrivez 'quinze virgule trois' en chiffres",
                    "Comparez: 7,2 et 7,21",
                    "Identifiez les dixièmes dans 4,567"
                ]
            },
            {
                "id": "MATH_002",
                "titre": "Les opérations avec les décimaux",
                "domaine": "Nombres et Calculs",
                "objectifs": [
                    "Additionner des nombres décimaux",
                    "Soustraire des nombres décimaux",
                    "Calculer correctement en plaçant la virgule"
                ],
                "contenu": """
## Additionner des décimaux

La règle principale: **Aligner les virgules!**

### Exemple: 12,5 + 7,3

```
  12,5
+  7,3
------
  19,8
```

### Étapes:
1. Aligner les virgules verticalement
2. Additionner colonne par colonne (de droite à gauche)
3. Placer la virgule au même endroit

## Soustraire des décimaux

La même règle s'applique: **Aligner les virgules!**

### Exemple: 15,7 - 8,2

```
  15,7
-  8,2
------
   7,5
```

### Cas où il faut emprunter:

Exemple: 12,3 - 5,8

```
  12,3
-  5,8
------
   6,5
```

Comme 3 < 8, on emprunte 1 à la partie entière: 13 - 8 = 5, mais on doit aussi compter 3

## Astuces

- Toujours aligner les virgules avant de calculer
- Vérifier que le résultat a du sens (plus grand pour une addition, plus petit pour une soustraction)
- Utiliser du papier brouillon pour bien présenter le calcul
""",
                "concepts_cles": {
                    "Virgule": "Doit être alignée lors du calcul",
                    "Addition": "Augmente le nombre",
                    "Soustraction": "Diminue le nombre",
                    "Emprunt": "Technique pour soustraire quand le chiffre du bas > chiffre du haut"
                },
                "exercices_exemples": [
                    "Calculez: 23,5 + 12,7",
                    "Calculez: 50,2 - 15,8",
                    "Posez et calculez: 8,34 + 12,56"
                ]
            }
        ]
    },

    "anglais": {
        "matiere": "Anglais",
        "niveau": "6ème",
        "courses": [
            {
                "id": "EN_001",
                "titre": "Se présenter en anglais",
                "domaine": "Production orale",
                "objectifs": [
                    "Dire son nom en anglais",
                    "Donner son âge",
                    "Dire d'où on vient",
                    "Parler de ses loisirs"
                ],
                "contenu": """
## Présentation de base

### 1. Dire bonjour et son nom

**Anglais:**
"Hello, my name is John."

**Français:**
"Bonjour, je m'appelle John."

**Structure:**
Hello / Hi + my name is + [nom]

### 2. Dire son âge

**Anglais:**
"I am 12 years old."

**Français:**
"J'ai 12 ans." (littéralement: "Je suis 12 ans vieux")

**Structure:**
I am + [nombre] + years old

### 3. Dire d'où on vient

**Anglais:**
"I am from France."

**Français:**
"Je viens de France."

**Pays courants:**
- France = France
- England = Angleterre
- Spain = Espagne
- Germany = Allemagne
- Italy = Italie

### 4. Parler de ses loisirs

**Anglais:**
"I like football."
"I like reading."
"I like swimming."

**Structure:**
I like + [verbe-ing] ou [nom]

## Conversation complète

**A:** Hello! My name is Sophie. I am 12 years old. I am from France.
**B:** Hi Sophie! Nice to meet you.
**A:** What about you?
**B:** My name is Tom. I am 11 years old. I am from England. I like football.
**A:** That's great! I like reading.
""",
                "concepts_cles": {
                    "Hello": "Bonjour",
                    "My name is": "Je m'appelle",
                    "I am": "Je suis / J'ai (pour l'âge)",
                    "From": "De (provenance)",
                    "Like": "Aimer"
                },
                "exercices_exemples": [
                    "Présentez-vous en anglais (nom, âge, provenance)",
                    "Parlez de trois choses que vous aimez",
                    "Écoutez et complétez une présentation"
                ]
            }
        ]
    },

    "histoire_geographie": {
        "matiere": "Histoire-Géographie",
        "niveau": "6ème",
        "courses": [
            {
                "id": "HG_001",
                "titre": "S'orienter sur une carte",
                "domaine": "Géographie",
                "objectifs": [
                    "Comprendre les points cardinaux",
                    "Lire les coordonnées sur une carte",
                    "Se repérer en utilisant une carte"
                ],
                "contenu": """
## Les points cardinaux

Il existe 4 points cardinaux qui permettent de s'orienter:

### Nord (N)
- Vers le haut d'une carte
- Où le soleil ne va jamais très haut

### Sud (S)
- Vers le bas d'une carte
- Opposé du Nord

### Est (E)
- Vers la droite d'une carte
- Où le soleil se lève

### Ouest (O)
- Vers la gauche d'une carte
- Où le soleil se couche

## Les points cardinaux intermédiaires

Entre les quatre points cardinaux, il y a des directions intermédiaires:
- Nord-Est (NE)
- Nord-Ouest (NO)
- Sud-Est (SE)
- Sud-Ouest (SO)

## Comment utiliser une boussole?

1. Tenir la boussole horizontalement
2. L'aiguille rouge pointe toujours vers le Nord
3. Tourner la carte pour aligner le Nord de la carte avec l'aiguille
4. Vous pouvez maintenant lire la carte correctement

## Lire les coordonnées géographiques

Chaque point sur Terre peut être localisé avec:
- **Latitude**: Distance par rapport à l'équateur (0° à 90° Nord ou Sud)
- **Longitude**: Distance par rapport au méridien de Greenwich (0° à 180° Est ou Ouest)

### Exemple:
Paris = 48,5° N, 2,3° E
- 48,5° Nord = 48,5° au-dessus de l'équateur
- 2,3° Est = 2,3° à l'est du méridien de Greenwich
""",
                "concepts_cles": {
                    "Points cardinaux": "Nord, Sud, Est, Ouest - directions fondamentales",
                    "Équateur": "Ligne imaginaire qui divise la Terre en deux",
                    "Méridien": "Ligne imaginaire du Nord au Sud",
                    "Latitude": "Position par rapport à l'équateur",
                    "Longitude": "Position par rapport au méridien de Greenwich"
                },
                "exercices_exemples": [
                    "Sur une carte de France, où est la Bretagne par rapport à Paris?",
                    "Identifiez les pays au Nord de la France",
                    "Utilisez une boussole pour vous orienter"
                ]
            }
        ]
    },

    "sciences_technologie": {
        "matiere": "Sciences et Technologie",
        "niveau": "6ème",
        "courses": [
            {
                "id": "SC_001",
                "titre": "La cellule: unité de la vie",
                "domaine": "Sciences de la Vie et de la Terre (SVT)",
                "objectifs": [
                    "Comprendre qu'tous les êtres vivants sont faits de cellules",
                    "Connaître les parties d'une cellule",
                    "Différencier les cellules animales et végétales"
                ],
                "contenu": """
## Qu'est-ce qu'une cellule?

La cellule est la plus petite unité de vie. Tous les êtres vivants sont composés d'au moins une cellule.

### Exemples:
- Un humain: 37 milliards de cellules!
- Une bactérie: 1 cellule seulement
- Une plante: des millions de cellules

## Les trois règles de la cellule

### 1. Théorie cellulaire
Tous les êtres vivants sont composés de cellules.

### 2. Toutes les cellules viennent de cellules
Les cellules se reproduisent par division.

### 3. La cellule est l'unité de vie
C'est la plus petite unité qui peut vivre seule.

## Les parties d'une cellule

### Membrane cellulaire
- Enveloppe qui entoure la cellule
- Contrôle ce qui entre et sort

### Noyau
- Centre de commande de la cellule
- Contient l'ADN (information génétique)

### Cytoplasme
- Matière gélatineuse à l'intérieur
- Contient les autres structures

### Mitochondrie
- "Centrale électrique" de la cellule
- Produit l'énergie

## Cellule animale vs Cellule végétale

### Cellule animale:
- Membrane cellulaire
- Noyau
- Mitochondries
- Forme ronde/irrégulière

### Cellule végétale:
- **Paroi cellulaire** (en plus de la membrane)
- **Chloroplaste** (pour la photosynthèse)
- **Vacuole** (stockage)
- Forme rectangulaire
""",
                "concepts_cles": {
                    "Cellule": "Plus petite unité de vie",
                    "Membrane": "Enveloppe de la cellule",
                    "Noyau": "Centre de commande",
                    "Mitochondrie": "Centrale électrique de la cellule",
                    "Chloroplaste": "Produit l'énergie chez les plantes"
                },
                "exercices_exemples": [
                    "Dessinez une cellule animale avec ses parties",
                    "Comparez une cellule animale et végétale",
                    "Expliquez pourquoi les cellules sont importantes pour la vie"
                ]
            }
        ]
    }
}

def generate_courses():
    """Génère les fichiers de cours"""
    print("=" * 70)
    print("GÉNÉRATION DES COURS AVEC CONTENU PÉDAGOGIQUE")
    print("=" * 70)

    total_courses = 0

    for matiere, data in COURSES_DATA.items():
        print(f"\n📚 {data['matiere']}")

        courses_list = data['courses']

        # Sauvegarde
        filename = f"{matiere}_courses_6eme.json"
        filepath = OUTPUT_DIR / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                "matiere": data['matiere'],
                "niveau": data['niveau'],
                "total_courses": len(courses_list),
                "courses": courses_list
            }, f, ensure_ascii=False, indent=2)

        print(f"   ✅ {len(courses_list)} cours générés")
        print(f"   📁 {filename}")
        total_courses += len(courses_list)

    print("\n" + "=" * 70)
    print(f"✅ SUCCÈS: {total_courses} cours générés avec contenu pédagogique!")
    print(f"📂 Location: {OUTPUT_DIR}")
    print("=" * 70)

if __name__ == "__main__":
    generate_courses()
