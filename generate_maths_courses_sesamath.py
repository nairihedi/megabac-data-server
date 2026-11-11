#!/usr/bin/env python3
"""
Génération des cours de Mathématiques 6ème basés sur Sesamath
Source: https://manuel.sesamath.net/numerique/?ouvrage=cm6_2025
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("./data/courses")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Structure basée sur Sesamath CM6 2025
MATHS_COURSES_SESAMATH = {
    "matiere": "Mathématiques",
    "niveau": "6ème",
    "source": "Sesamath - Cahier 6e 2025",
    "source_url": "https://manuel.sesamath.net/numerique/?ouvrage=cm6_2025",
    "courses": [
        {
            "id": "MATH_N1_001",
            "titre": "Nombres entiers et décimaux",
            "domaine": "N - Nombres, calcul et résolution de problèmes",
            "section": "N1",
            "objectifs": [
                "Comprendre le tableau de numération",
                "Lire et écrire les nombres décimaux",
                "Comprendre la position des chiffres"
            ],
            "contenu": """
## À RETENIR

### Tableau de numération
Le tableau de numération permet de bien lire et écrire les nombres en repérant la position de chaque chiffre.

Les classes de nombres:
- **Milliards**: unités de milliards, dizaines de milliards, centaines de milliards
- **Millions**: unités de millions, dizaines de millions, centaines de millions
- **Milliers**: unités de milliers, dizaines de milliers, centaines de milliers
- **Unités**: unités, dizaines, centaines

### Nombre décimal
Un nombre possédant à écrire sous la forme d'une fraction décimale: fraction ayant pour numérateur un nombre entier et pour dénominateur 1: 10; 100; 1 000...

L'écriture décimale est la somme de sa partie entière et de sa partie décimale.

### Exemple
1 345,87 = 1 345 + 87/100
- Partie entière: 1 345
- Partie décimale: 87 centièmes (0,87)

### Comparer, ranger, intercaler, encadrer
- **Comparer**: trouver le plus petit ou le plus grand entre deux nombres
- **Ranger**: ordonner des nombres dans l'ordre croissant (respectivement décroissant, du plus grand au plus petit)
- **Intercaler**: placer un nombre entre deux autres nombres
- **Encadrer**: trouver deux nombres tels que le nombre soit compris entre ces deux nombres (l'inférieur et l'autre supérieur ou le contraire!)

⚠️ Attention à ne pas confondre le chiffre des dizaines et le nombre de dizaines!
""",
            "concepts_cles": {
                "Tableau de numération": "Outil pour lire et placer les nombres selon la position de leurs chiffres",
                "Nombre décimal": "Nombre avec une partie entière et une partie décimale",
                "Partie entière": "Les chiffres avant la virgule",
                "Partie décimale": "Les chiffres après la virgule",
                "Dixième": "1/10 = 0,1",
                "Centième": "1/100 = 0,01",
                "Millième": "1/1000 = 0,001"
            },
            "exercices_propositions": [
                "Placer 1 345,87 sur un tableau de numération",
                "Comparer 3,45 et 3,54",
                "Ranger en ordre croissant: 5,3 - 5,03 - 5,33 - 5,303",
                "Intercaler un nombre entre 2,3 et 2,4"
            ]
        },
        {
            "id": "MATH_N2_001",
            "titre": "Fractions",
            "domaine": "N - Nombres, calcul et résolution de problèmes",
            "section": "N2",
            "objectifs": [
                "Comprendre la notion de fraction",
                "Utiliser les fractions pour mesurer",
                "Comparer et ranger des fractions"
            ],
            "contenu": """
## Qu'est-ce qu'une fraction?

Une fraction est une partie d'un tout. Elle est écrite avec deux nombres:
- **Numérateur** (en haut): le nombre de parts prises
- **Dénominateur** (en bas): le nombre total de parts

### Exemple
3/4 signifie: 3 parts sur 4 parts égales

## Fractions particulières

### Fraction = 1
Si numérateur = dénominateur, la fraction = 1
Exemple: 5/5 = 1

### Fraction < 1
Si numérateur < dénominateur
Exemple: 3/5 < 1

### Fraction > 1
Si numérateur > dénominateur
Exemple: 7/5 > 1

## Utiliser les fractions pour mesurer

Les fractions servent à mesurer des grandeurs:
- 1/2 litre = 0,5 litre
- 3/4 heure = 45 minutes
- 1/4 kilogramme = 250 grammes

## Comparer des fractions

Pour comparer des fractions avec le même dénominateur:
- 3/7 < 5/7 (car 3 < 5)

Pour comparer des fractions avec le même numérateur:
- 3/7 > 3/8 (car 7 < 8, donc les parts sont plus grandes)
""",
            "concepts_cles": {
                "Fraction": "Partie d'un tout, représentée par numérateur/dénominateur",
                "Numérateur": "Nombre de parts prises",
                "Dénominateur": "Nombre total de parts égales",
                "Fraction = 1": "Quand numérateur = dénominateur",
                "Fraction < 1": "Quand numérateur < dénominateur",
                "Fraction > 1": "Quand numérateur > dénominateur"
            },
            "exercices_propositions": [
                "Représenter 3/4 par un dessin",
                "Comparer 2/3 et 2/5",
                "Calculer 1/2 de 12",
                "Ranger: 1/2, 1/3, 1/4, 1/5 en ordre croissant"
            ]
        },
        {
            "id": "MATH_G1_001",
            "titre": "Configurations planes - Angles et distances",
            "domaine": "G - Espace et géométrie",
            "section": "G1",
            "objectifs": [
                "Identifier les angles dans une figure",
                "Mesurer des angles",
                "Tracer et comparer des distances"
            ],
            "contenu": """
## Les angles

### Qu'est-ce qu'un angle?
Un angle est formé par deux demi-droites qui partent d'un même point (le sommet).

Les deux demi-droites s'appellent les **côtés** de l'angle.

### Types d'angles

**Angle droit**: mesure 90°
- Angle formé par deux droites perpendiculaires

**Angle aigu**: mesure moins de 90°
- Angle plus petit qu'un angle droit

**Angle obtus**: mesure entre 90° et 180°
- Angle plus grand qu'un angle droit mais plus petit qu'une ligne droite

**Angle plat**: mesure 180°
- C'est une ligne droite

## Mesurer un angle

On utilise un **rapporteur** pour mesurer les angles.

Étapes:
1. Placer le centre du rapporteur sur le sommet de l'angle
2. Aligner le 0° du rapporteur avec l'un des côtés
3. Lire le nombre de degrés où l'autre côté croise le rapporteur

## Distances

Une distance est la mesure de l'espace entre deux points.

La **distance la plus courte** entre deux points est la ligne droite qui les relie.
""",
            "concepts_cles": {
                "Angle": "Deux demi-droites qui partent du même point",
                "Sommet": "Le point de départ des deux côtés",
                "Côtés": "Les deux demi-droites de l'angle",
                "Degré": "Unité de mesure des angles (°)",
                "Rapporteur": "Outil pour mesurer les angles",
                "Angle droit": "90°",
                "Angle aigu": "< 90°",
                "Angle obtus": "> 90° et < 180°"
            },
            "exercices_propositions": [
                "Mesurer un angle avec le rapporteur",
                "Identifier les angles dans une figure géométrique",
                "Tracer un angle de 45°",
                "Comparer deux angles"
            ]
        },
        {
            "id": "MATH_M1_001",
            "titre": "Longueurs, masses, contenances",
            "domaine": "M - Grandeurs et mesures",
            "section": "M1",
            "objectifs": [
                "Connaître les unités de longueur, masse et contenance",
                "Convertir entre les unités",
                "Résoudre des problèmes de mesure"
            ],
            "contenu": """
## Les unités de longueur

La **longueur** est la distance entre deux points.

**Unités principales:**
- Kilomètre (km) = 1 000 m
- Hectomètre (hm) = 100 m
- Décamètre (dam) = 10 m
- **Mètre (m)** = unité de référence
- Décimètre (dm) = 0,1 m
- Centimètre (cm) = 0,01 m
- Millimètre (mm) = 0,001 m

**Tableau de conversion:**
```
km | hm | dam | m | dm | cm | mm
 1 |    |     | 1 0 0 0  |
```

Pour convertir: multiplier par 10 (vers la droite) ou diviser par 10 (vers la gauche)

Exemple: 2,5 m = 250 cm (× 100)

## Les unités de masse

La **masse** est la quantité de matière d'un objet.

**Unités principales:**
- Kilogramme (kg)
- Hectogramme (hg)
- Décagramme (dag)
- **Gramme (g)** = unité de référence
- Décigramme (dg)
- Centigramme (cg)
- Milligramme (mg)

## Les unités de contenance

La **contenance** (ou volume liquide) est la capacité d'un récipient.

**Unités principales:**
- **Litre (L)** = unité de référence
- Décilitre (dL) = 0,1 L
- Centilitre (cL) = 0,01 L
- Millilitre (mL) = 0,001 L
- Décalitre (daL) = 10 L
- Hectolitre (hL) = 100 L
""",
            "concepts_cles": {
                "Longueur": "Distance entre deux points",
                "Mètre": "Unité de référence pour la longueur",
                "Masse": "Quantité de matière",
                "Gramme": "Unité de référence pour la masse",
                "Contenance": "Capacité d'un récipient",
                "Litre": "Unité de référence pour la contenance",
                "Conversion": "Passage d'une unité à l'autre"
            },
            "exercices_propositions": [
                "Convertir 2,5 km en mètres",
                "Ranger en ordre croissant: 1 200 g, 1,2 kg, 12 dag",
                "Une bouteille contient 1,5 L. Combien de millilitres?",
                "Un car pèse 5 tonnes. Convertir en kilogrammes"
            ]
        }
    ]
}

def generate_maths_courses():
    """Génère les fichiers JSON de courses mathématiques basés sur Sesamath"""
    print("=" * 70)
    print("GÉNÉRATION DES COURS DE MATHÉMATIQUES BASÉS SUR SESAMATH")
    print("=" * 70)

    filename = "mathematiques_courses_sesamath_6eme.json"
    filepath = OUTPUT_DIR / filename

    # Sauvegarde
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump({
            "matiere": MATHS_COURSES_SESAMATH["matiere"],
            "niveau": MATHS_COURSES_SESAMATH["niveau"],
            "source": MATHS_COURSES_SESAMATH["source"],
            "source_url": MATHS_COURSES_SESAMATH["source_url"],
            "total_courses": len(MATHS_COURSES_SESAMATH["courses"]),
            "courses": MATHS_COURSES_SESAMATH["courses"]
        }, f, ensure_ascii=False, indent=2)

    print(f"\n✅ {len(MATHS_COURSES_SESAMATH['courses'])} cours générés basés sur Sesamath")
    print(f"📁 {filename}")
    print(f"📍 Source: {MATHS_COURSES_SESAMATH['source_url']}")
    print("\nCours générés:")
    for course in MATHS_COURSES_SESAMATH["courses"]:
        print(f"  • {course['section']} - {course['titre']}")

    print("\n" + "=" * 70)
    print(f"✅ SUCCÈS: Cours mathématiques Sesamath générés!")
    print("=" * 70)

if __name__ == "__main__":
    generate_maths_courses()
