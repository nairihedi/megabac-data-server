#!/usr/bin/env python3
"""
Script de génération des structures JSON pour le curriculum 6ème
Étape 3: Structuration des données pédagogiques
"""

import json
from pathlib import Path
from datetime import datetime

# Dossier de sortie
OUTPUT_DIR = Path("./data/curricula")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Curriculum structuré pour chaque matière
CURRICULUM_DATA = {
    "francais": {
        "matiere": "Français",
        "niveau": "6ème",
        "programme_bo": "BO n° 16 du 17 avril 2025",
        "description": "Programme de français pour le cycle 3 (classe de 6ème)",
        "domaines_apprentissage": [
            {
                "id": "LO",
                "nom": "Langage oral",
                "description": "Développer l'écoute active et l'expression orale",
                "competences": [
                    {
                        "id": "LO.1",
                        "titre": "Écouter et comprendre",
                        "description": "Comprendre un message oral et identifier les informations principales"
                    },
                    {
                        "id": "LO.2",
                        "titre": "S'exprimer à l'oral",
                        "description": "Produire des énoncés clairs et adaptés à la situation de communication"
                    }
                ],
                "concepts_cles": ["Lexique", "Intonation", "Phonologie", "Enonciation"]
            },
            {
                "id": "LEC",
                "nom": "Lecture",
                "description": "Développer les compétences de compréhension et d'analyse de textes",
                "competences": [
                    {
                        "id": "LEC.1",
                        "titre": "Lire et comprendre",
                        "description": "Identifier le sens global et les détails importants d'un texte"
                    },
                    {
                        "id": "LEC.2",
                        "titre": "Analyser un texte",
                        "description": "Identifier la structure et les procédés d'écriture d'un texte"
                    }
                ],
                "concepts_cles": ["Texte narratif", "Texte descriptif", "Personnage", "Intrigue"]
            },
            {
                "id": "ECR",
                "nom": "Écriture",
                "description": "Développer les compétences de production écrite",
                "competences": [
                    {
                        "id": "ECR.1",
                        "titre": "Rédiger un texte",
                        "description": "Produire un texte cohérent et structuré selon une intention"
                    },
                    {
                        "id": "ECR.2",
                        "titre": "Réviser son écrit",
                        "description": "Relire et corriger un texte pour améliorer sa qualité"
                    }
                ],
                "concepts_cles": ["Structure narrative", "Ponctuation", "Orthographe", "Cohérence"]
            },
            {
                "id": "EL",
                "nom": "Étude de la langue",
                "description": "Acquérir les outils pour analyser et bien former la langue",
                "competences": [
                    {
                        "id": "EL.1",
                        "titre": "Orthographe",
                        "description": "Maîtriser les règles d'orthographe grammaticale et lexicale"
                    },
                    {
                        "id": "EL.2",
                        "titre": "Grammaire",
                        "description": "Identifier et analyser les constituants d'une phrase"
                    },
                    {
                        "id": "EL.3",
                        "titre": "Vocabulaire",
                        "description": "Enrichir son vocabulaire et comprendre la formation des mots"
                    }
                ],
                "concepts_cles": ["Phrase simple", "Verbe", "Sujet", "Accord", "Complément"]
            },
            {
                "id": "LIT",
                "nom": "Littérature et imaginaire",
                "description": "Développer la culture littéraire et l'imagination",
                "competences": [
                    {
                        "id": "LIT.1",
                        "titre": "Lire des œuvres",
                        "description": "Découvrir différents genres littéraires et œuvres majeures"
                    },
                    {
                        "id": "LIT.2",
                        "titre": "Analyser un récit",
                        "description": "Identifier les éléments caractéristiques d'une histoire"
                    }
                ],
                "concepts_cles": ["Conte", "Légende", "Roman", "Nouvelle", "Héros"]
            }
        ],
        "progression_annuelle": [
            {
                "trimestre": 1,
                "titre": "Trimestre 1 - Septembre à novembre",
                "themes": ["Accueil - Se présenter", "Les genres littéraires", "Communication orale"]
            },
            {
                "trimestre": 2,
                "titre": "Trimestre 2 - Décembre à février",
                "themes": ["Récit et aventure", "Analyse de textes", "Projet d'écriture"]
            },
            {
                "trimestre": 3,
                "titre": "Trimestre 3 - Mars à juin",
                "themes": ["Littérature jeunesse", "Expression créative", "Bilan et projets finaux"]
            }
        ],
        "evaluation": {
            "types_exercices": [
                "Compréhension orale",
                "Expression orale",
                "Compréhension écrite",
                "Production écrite",
                "Analyse grammaticale",
                "Vocabulaire"
            ],
            "criteres_evaluation": [
                "Compréhension du message",
                "Clarté de l'expression",
                "Qualité de la structure",
                "Respectdes règles de la langue",
                "Richesse du vocabulaire"
            ]
        },
        "sources": {
            "programme_officiel": "Bulletin Officiel n° 16 du 17 avril 2025",
            "ressources_eduscol": "https://eduscol.education.gouv.fr/4800/ressources-d-accompagnement-du-programme-de-francais-au-cycle-3"
        }
    },

    "mathematiques": {
        "matiere": "Mathématiques",
        "niveau": "6ème",
        "programme_bo": "BO n° 16 du 17 avril 2025",
        "description": "Programme de mathématiques pour le cycle 3 (classe de 6ème)",
        "domaines_apprentissage": [
            {
                "id": "NC",
                "nom": "Nombres et Calculs",
                "description": "Maîtriser la manipulation des nombres et les opérations",
                "competences": [
                    {
                        "id": "NC.1",
                        "titre": "Comprendre les nombres décimaux",
                        "description": "Lire, écrire et comparer les nombres décimaux"
                    },
                    {
                        "id": "NC.2",
                        "titre": "Opérations",
                        "description": "Additionner, soustraire, multiplier et diviser"
                    },
                    {
                        "id": "NC.3",
                        "titre": "Fractions",
                        "description": "Comprendre et utiliser les fractions"
                    }
                ],
                "concepts_cles": ["Nombre entier", "Nombre décimal", "Fraction", "Pourcentage"]
            },
            {
                "id": "GEO",
                "nom": "Géométrie",
                "description": "Développer le raisonnement géométrique",
                "competences": [
                    {
                        "id": "GEO.1",
                        "titre": "Propriétés géométriques",
                        "description": "Identifier et utiliser les propriétés des formes"
                    },
                    {
                        "id": "GEO.2",
                        "titre": "Constructions géométriques",
                        "description": "Construire et représenter des figures"
                    },
                    {
                        "id": "GEO.3",
                        "titre": "Symétries et transformations",
                        "description": "Comprendre les symétries et les transformations géométriques"
                    }
                ],
                "concepts_cles": ["Point", "Droite", "Angle", "Triangle", "Polygone", "Symétrie"]
            },
            {
                "id": "GM",
                "nom": "Grandeurs et Mesures",
                "description": "Développer la compréhension des grandeurs et des mesures",
                "competences": [
                    {
                        "id": "GM.1",
                        "titre": "Longueurs et distances",
                        "description": "Mesurer et calculer des distances"
                    },
                    {
                        "id": "GM.2",
                        "titre": "Aires et volumes",
                        "description": "Calculer des aires et des volumes"
                    },
                    {
                        "id": "GM.3",
                        "titre": "Durées et temps",
                        "description": "Lire l'heure et calculer des durées"
                    }
                ],
                "concepts_cles": ["Unité de mesure", "Longueur", "Aire", "Volume", "Temps"]
            }
        ],
        "progression_annuelle": [
            {
                "trimestre": 1,
                "titre": "Trimestre 1 - Nombres et opérations",
                "themes": ["Nombres entiers et décimaux", "Opérations de base"]
            },
            {
                "trimestre": 2,
                "titre": "Trimestre 2 - Géométrie",
                "themes": ["Formes et figures", "Constructions géométriques"]
            },
            {
                "trimestre": 3,
                "titre": "Trimestre 3 - Grandeurs et applications",
                "themes": ["Mesures", "Problèmes concrets"]
            }
        ],
        "evaluation": {
            "types_exercices": [
                "Calcul mental",
                "Calcul posé",
                "Résolution de problèmes",
                "Constructions géométriques",
                "Mesures et calcul de grandeurs"
            ],
            "criteres_evaluation": [
                "Compréhension du problème",
                "Procédure de résolution",
                "Exactitude du résultat",
                "Justification de la réponse",
                "Précision des constructions"
            ]
        },
        "sources": {
            "programme_officiel": "Bulletin Officiel n° 16 du 17 avril 2025",
            "pdf_telechargé": "data/pdfs_programmes/02_MATHEMATIQUES_cycle3.pdf"
        }
    },

    "anglais": {
        "matiere": "Anglais (Langues vivantes étrangères)",
        "niveau": "6ème",
        "programme_bo": "BO n° 22 du 29 mai 2025",
        "description": "Programme de langues vivantes étrangères pour le cycle 3 (classe de 6ème)",
        "niveau_cecrl": "A1",
        "domaines_apprentissage": [
            {
                "id": "CO",
                "nom": "Compréhension orale",
                "description": "Développer l'écoute et la compréhension de l'anglais",
                "competences": [
                    {
                        "id": "CO.1",
                        "titre": "Écouter et identifier",
                        "description": "Identifier des mots clés dans un document audio"
                    },
                    {
                        "id": "CO.2",
                        "titre": "Comprendre un message",
                        "description": "Comprendre le sens global d'un énoncé"
                    }
                ],
                "concepts_cles": ["Phonétique", "Accent tonique", "Intonation"]
            },
            {
                "id": "PO",
                "nom": "Production orale",
                "description": "Développer la parole et l'expression orale",
                "competences": [
                    {
                        "id": "PO.1",
                        "titre": "Prononcer correctement",
                        "description": "Produire des sons et des mots correctement"
                    },
                    {
                        "id": "PO.2",
                        "titre": "S'exprimer",
                        "description": "Produire des énoncés simples"
                    }
                ],
                "concepts_cles": ["Prononciation", "Accentuation", "Rythme"]
            },
            {
                "id": "CE",
                "nom": "Compréhension écrite",
                "description": "Développer la lecture et la compréhension de textes anglais",
                "competences": [
                    {
                        "id": "CE.1",
                        "titre": "Lire et identifier",
                        "description": "Identifier des informations dans un texte écrit"
                    }
                ],
                "concepts_cles": ["Vocabulaire", "Structures grammaticales"]
            },
            {
                "id": "PE",
                "nom": "Production écrite",
                "description": "Développer l'écriture en anglais",
                "competences": [
                    {
                        "id": "PE.1",
                        "titre": "Écrire",
                        "description": "Produire des énoncés simples à l'écrit"
                    }
                ],
                "concepts_cles": ["Orthographe", "Structures de base"]
            }
        ],
        "vocabulaire_themes": [
            "Présentation personnelle",
            "Famille",
            "Animaux",
            "Aliments",
            "Habitat",
            "Vêtements",
            "Loisirs"
        ],
        "structures_grammaticales": [
            "Présent simple du verbe 'to be'",
            "Présent simple du verbe 'have got'",
            "Verbes d'action simples",
            "Pluriels réguliers",
            "Articles (a, an, the)"
        ],
        "evaluation": {
            "types_exercices": [
                "Compréhension orale",
                "Prononciation",
                "Vocabulaire",
                "Structures grammaticales",
                "Production orale simple",
                "Production écrite simple"
            ]
        },
        "sources": {
            "programme_officiel": "Bulletin Officiel n° 22 du 29 mai 2025"
        }
    },

    "histoire_geographie": {
        "matiere": "Histoire-Géographie",
        "niveau": "6ème",
        "programme_bo": "BO n° 31 du 30 juillet 2020",
        "description": "Programme d'histoire-géographie pour le cycle 3 (classe de 6ème)",
        "disciplines": ["Histoire", "Géographie"],
        "domaines_apprentissage": [
            {
                "id": "HIS",
                "nom": "Histoire",
                "description": "Comprendre le passé et développer le sens historique",
                "competences": [
                    {
                        "id": "HIS.1",
                        "titre": "Périodes historiques",
                        "description": "Situer des événements dans le temps"
                    },
                    {
                        "id": "HIS.2",
                        "titre": "Sources historiques",
                        "description": "Analyser des documents historiques"
                    }
                ],
                "periodes": [
                    "Préhistoire",
                    "Antiquité",
                    "Moyen Âge",
                    "Époque moderne",
                    "Époque contemporaine"
                ],
                "concepts_cles": ["Chronologie", "Cause et conséquence", "Civilisations", "Changements"]
            },
            {
                "id": "GEO",
                "nom": "Géographie",
                "description": "Comprendre l'espace et ses enjeux",
                "competences": [
                    {
                        "id": "GEO.1",
                        "titre": "Orientation et localisation",
                        "description": "Se repérer dans l'espace à différentes échelles"
                    },
                    {
                        "id": "GEO.2",
                        "titre": "Paysages et territoires",
                        "description": "Décrire et analyser les paysages"
                    },
                    {
                        "id": "GEO.3",
                        "titre": "Enjeux géographiques",
                        "description": "Comprendre les enjeux humains et naturels"
                    }
                ],
                "themes": [
                    "Localisation et représentation",
                    "Habiter le monde",
                    "Mers et océans",
                    "Densités et peuplement",
                    "Ressources naturelles"
                ],
                "concepts_cles": ["Latitude", "Longitude", "Équateur", "Tropiques", "Climat", "Population"]
            }
        ],
        "evaluation": {
            "types_exercices": [
                "Questionnaires de compréhension",
                "Analyse de documents",
                "Cartes et représentations",
                "Frises chronologiques",
                "Descriptions de paysages"
            ]
        },
        "sources": {
            "programme_officiel": "Bulletin Officiel n° 31 du 30 juillet 2020"
        }
    },

    "sciences_technologie": {
        "matiere": "Sciences et Technologie",
        "niveau": "6ème",
        "programme_bo": "BO n° 25 du 22 juin 2023",
        "description": "Programme de sciences et technologie pour le cycle 3 (classe de 6ème) - Regroupé SVT + Physique-Chimie",
        "note": "Éduscol regroupe SVT, Physique-Chimie et Technologie. Pour Megabac, ils seront potentiellement séparés.",
        "domaines_apprentissage": [
            {
                "id": "SVT",
                "nom": "Sciences de la Vie et de la Terre (SVT)",
                "description": "Comprendre le vivant et l'environnement",
                "competences": [
                    {
                        "id": "SVT.1",
                        "titre": "Organisation du vivant",
                        "description": "Comprendre la structure et la fonction des êtres vivants"
                    },
                    {
                        "id": "SVT.2",
                        "titre": "Écosystèmes",
                        "description": "Analyser les relations dans un écosystème"
                    },
                    {
                        "id": "SVT.3",
                        "titre": "Santé",
                        "description": "Comprendre l'hygiène et la santé"
                    }
                ],
                "themes": [
                    "La matière vivante",
                    "Croissance et reproduction",
                    "Chaîne alimentaire",
                    "Écosystèmes locaux",
                    "Biodiversité",
                    "Équilibre écologique"
                ],
                "concepts_cles": ["Cellule", "Photosynthèse", "Appareil digestif", "Biodiversité"]
            },
            {
                "id": "PC",
                "nom": "Physique-Chimie",
                "description": "Comprendre la matière et les transformations",
                "competences": [
                    {
                        "id": "PC.1",
                        "titre": "Matière et propriétés",
                        "description": "Identifier et classifier la matière"
                    },
                    {
                        "id": "PC.2",
                        "titre": "Transformations",
                        "description": "Comprendre les réactions chimiques"
                    },
                    {
                        "id": "PC.3",
                        "titre": "Énergie et forces",
                        "description": "Analyser les forces et l'énergie"
                    }
                ],
                "themes": [
                    "États de la matière",
                    "Changements d'états",
                    "Mélanges et solutions",
                    "Réactions chimiques simples",
                    "Sources d'énergie",
                    "Mouvements et forces"
                ],
                "concepts_cles": ["Atome", "Molécule", "Réaction chimique", "Énergie", "Force"]
            },
            {
                "id": "TECH",
                "nom": "Technologie",
                "description": "Comprendre les objets et systèmes techniques",
                "competences": [
                    {
                        "id": "TECH.1",
                        "titre": "Design et production",
                        "description": "Analyser et concevoir des objets"
                    },
                    {
                        "id": "TECH.2",
                        "titre": "Systèmes et automatis",
                        "description": "Comprendre le fonctionnement des systèmes"
                    }
                ],
                "themes": [
                    "Objets et matériaux",
                    "Énergie et puissance",
                    "Automatismes",
                    "Programmation simple"
                ],
                "concepts_cles": ["Fonction technique", "Énergie", "Capteur", "Actionneur"]
            }
        ],
        "evaluation": {
            "types_exercices": [
                "Observation et expérimentation",
                "Analyse de phénomènes",
                "Schémas et diagrammes",
                "Résolution de problèmes",
                "Projets techniques"
            ]
        },
        "sources": {
            "programme_officiel": "Bulletin Officiel n° 25 du 22 juin 2023"
        }
    }
}

def save_curriculum_json():
    """Sauvegarde les données du curriculum en JSON"""
    print("=" * 60)
    print("ÉTAPE 3 - Génération des structures JSON du curriculum")
    print("=" * 60)
    print(f"\nDossier de destination: {OUTPUT_DIR.absolute()}\n")

    for matiere, data in CURRICULUM_DATA.items():
        filename = f"{matiere}_curriculum_6eme.json"
        filepath = OUTPUT_DIR / filename

        # Ajoute des métadonnées
        data["_metadata"] = {
            "created_at": datetime.now().isoformat(),
            "version": "1.0",
            "format": "JSON Curriculum"
        }

        # Sauvegarde en JSON
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ {filename}")
        print(f"   Domaines: {len(data['domaines_apprentissage'])}")
        print(f"   Taille: {filepath.stat().st_size / 1024:.1f} KB\n")

    print("=" * 60)
    print(f"✅ {len(CURRICULUM_DATA)} fichiers JSON générés avec succès!")
    print("=" * 60)

if __name__ == "__main__":
    save_curriculum_json()
