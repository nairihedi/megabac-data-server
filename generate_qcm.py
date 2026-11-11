#!/usr/bin/env python3
"""
Script de génération des QCM à partir du curriculum
Étape 4: Génération d'exercices QCM
"""

import json
from pathlib import Path
from typing import List, Dict
import random

# Configuration
CURRICULUM_DIR = Path("./data/curricula")
OUTPUT_DIR = Path("./data/exercices/qcm")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# QCM Templates par matière et domaine
QCM_TEMPLATES = {
    "francais": {
        "LO": [  # Langage oral
            {
                "template": "Qu'est-ce que la prononciation correcte d'un mot?",
                "type": "vocabulaire",
                "concepts": ["Prononciation", "Phonologie"],
                "reponse_index": 0,
                "explications": [
                    "C'est la manière de prononcer les sons d'un mot.",
                    "C'est l'écriture d'un mot.",
                    "C'est le sens d'un mot.",
                    "C'est la classe grammaticale d'un mot."
                ]
            },
            {
                "template": "Quel est le rôle de l'intonation dans la communication orale?",
                "type": "comprehension",
                "concepts": ["Intonation", "Énonciation"],
                "reponse_index": 1,
                "explications": [
                    "À corriger l'orthographe.",
                    "À exprimer des émotions et à nuancer le sens.",
                    "À accélérer la parole.",
                    "À augmenter le volume de la voix."
                ]
            },
            {
                "template": "Identifier le lexique approprié: Quel mot convient à 'une personne qui aime lire'?",
                "type": "vocabulaire",
                "concepts": ["Lexique"],
                "reponse_index": 2,
                "explications": [
                    "Un dormeur",
                    "Un sportif",
                    "Un lecteur passionné",
                    "Un travailleur"
                ]
            }
        ],
        "LEC": [  # Lecture
            {
                "template": "Qu'est-ce qu'un texte narratif?",
                "type": "comprehension",
                "concepts": ["Texte narratif", "Intrigue"],
                "reponse_index": 1,
                "explications": [
                    "Un texte qui décrit un lieu.",
                    "Un texte qui raconte une histoire avec des personnages et des événements.",
                    "Un texte qui explique un concept.",
                    "Un texte qui donne une opinion."
                ]
            },
            {
                "template": "Quel élément est essentiel dans une histoire?",
                "type": "vocabulaire",
                "concepts": ["Personnage", "Intrigue"],
                "reponse_index": 0,
                "explications": [
                    "Un personnage principal pour mener l'action.",
                    "Une longueur de 100 pages minimum.",
                    "Une morale à la fin.",
                    "Un titre en majuscules."
                ]
            }
        ],
        "ECR": [  # Écriture
            {
                "template": "Quel est le premier pas pour rédiger un bon texte?",
                "type": "comprehension",
                "concepts": ["Structure narrative", "Cohérence"],
                "reponse_index": 2,
                "explications": [
                    "Corriger l'orthographe.",
                    "Écrire rapidement sans réfléchir.",
                    "Planifier le contenu et la structure.",
                    "Ajouter des images."
                ]
            }
        ],
        "EL": [  # Étude de la langue
            {
                "template": "Qu'est-ce qu'un verbe dans une phrase?",
                "type": "vocabulaire",
                "concepts": ["Verbe", "Grammaire"],
                "reponse_index": 0,
                "explications": [
                    "Un mot qui exprime une action ou un état.",
                    "Un mot qui désigne une personne ou une chose.",
                    "Un mot qui complète le verbe.",
                    "Un mot invariable."
                ]
            },
            {
                "template": "Quel est le sujet de la phrase 'Le chat dort sur le canapé'?",
                "type": "comprehension",
                "concepts": ["Sujet", "Phrase simple"],
                "reponse_index": 1,
                "explications": [
                    "dort",
                    "Le chat",
                    "sur le canapé",
                    "le canapé"
                ]
            },
            {
                "template": "Comment s'appelle le mot qui modifie le nom?",
                "type": "vocabulaire",
                "concepts": ["Accord", "Grammaire"],
                "reponse_index": 2,
                "explications": [
                    "Un verbe",
                    "Un adverbe",
                    "Un adjectif",
                    "Un pronom"
                ]
            }
        ],
        "LIT": [  # Littérature
            {
                "template": "Qu'est-ce qu'un conte?",
                "type": "vocabulaire",
                "concepts": ["Conte", "Littérature"],
                "reponse_index": 0,
                "explications": [
                    "Un récit court avec des personnages souvent fantastiques.",
                    "Un long roman historique.",
                    "Une poésie avec des vers.",
                    "Un dialogue théâtral."
                ]
            },
            {
                "template": "Quel est le rôle du héros dans une histoire?",
                "type": "comprehension",
                "concepts": ["Héros", "Intrigue"],
                "reponse_index": 1,
                "explications": [
                    "Rester inactif.",
                    "Affronter des défis et avancer dans l'histoire.",
                    "Raconter l'histoire au lecteur.",
                    "Critiquer les autres personnages."
                ]
            }
        ]
    },

    "mathematiques": {
        "NC": [  # Nombres et Calculs
            {
                "template": "Qu'est-ce qu'un nombre décimal?",
                "type": "vocabulaire",
                "concepts": ["Nombre décimal"],
                "reponse_index": 1,
                "explications": [
                    "Un nombre entier toujours supérieur à 10.",
                    "Un nombre qui a une partie entière et une partie décimale séparées par une virgule.",
                    "Un nombre qui ne peut pas être divisé.",
                    "Un nombre négatif."
                ]
            },
            {
                "template": "Calculez: 12,5 + 7,3 = ?",
                "type": "calcul",
                "concepts": ["Opérations", "Nombre décimal"],
                "reponse_index": 2,
                "explications": [
                    "19,2",
                    "19,7",
                    "19,8",
                    "20,8"
                ]
            },
            {
                "template": "Qu'est-ce qu'une fraction?",
                "type": "vocabulaire",
                "concepts": ["Fraction"],
                "reponse_index": 0,
                "explications": [
                    "Une partie d'un tout, représentée par deux nombres (numérateur et dénominateur).",
                    "Un nombre toujours supérieur à 1.",
                    "Un nombre décimal arrondi.",
                    "Une opération de multiplication."
                ]
            }
        ],
        "GEO": [  # Géométrie
            {
                "template": "Combien de côtés a un triangle?",
                "type": "vocabulaire",
                "concepts": ["Triangle"],
                "reponse_index": 1,
                "explications": [
                    "2 côtés",
                    "3 côtés",
                    "4 côtés",
                    "5 côtés"
                ]
            },
            {
                "template": "Qu'est-ce qu'une symétrie?",
                "type": "comprehension",
                "concepts": ["Symétrie"],
                "reponse_index": 2,
                "explications": [
                    "Une rotation d'une figure.",
                    "Une augmentation de la taille d'une figure.",
                    "Une correspondance exacte de part et d'autre d'une droite.",
                    "Un déplacement d'une figure."
                ]
            }
        ],
        "GM": [  # Grandeurs et Mesures
            {
                "template": "Combien de centimètres dans un mètre?",
                "type": "vocabulaire",
                "concepts": ["Longueur"],
                "reponse_index": 3,
                "explications": [
                    "10 cm",
                    "50 cm",
                    "50 cm",
                    "100 cm"
                ]
            },
            {
                "template": "Quelle est l'unité pour mesurer une surface?",
                "type": "vocabulaire",
                "concepts": ["Aire"],
                "reponse_index": 1,
                "explications": [
                    "Le mètre (m)",
                    "Le mètre carré (m²)",
                    "Le litre (L)",
                    "Le kilogramme (kg)"
                ]
            }
        ]
    },

    "anglais": {
        "CO": [  # Compréhension orale
            {
                "template": "What is the correct pronunciation of 'water'?",
                "type": "vocabulaire",
                "concepts": ["Prononciation"],
                "reponse_index": 0,
                "explications": [
                    "/ˈwɔːtər/ (WO-ter)",
                    "/waɪ.tər/ (WAI-ter)",
                    "/wɑːt/ (WAT)",
                    "/wə.tɛr/ (WU-ter)"
                ]
            }
        ],
        "PO": [  # Production orale
            {
                "template": "How do you say 'Hello' in English?",
                "type": "vocabulaire",
                "concepts": ["Vocabulaire"],
                "reponse_index": 0,
                "explications": [
                    "Hello",
                    "Goodbye",
                    "Thank you",
                    "Please"
                ]
            }
        ],
        "CE": [  # Compréhension écrite
            {
                "template": "What is your name in English?",
                "type": "comprehension",
                "concepts": ["Structures de base"],
                "reponse_index": 0,
                "explications": [
                    "My name is...",
                    "I am name",
                    "Name is me",
                    "I name"
                ]
            }
        ],
        "PE": [  # Production écrite
            {
                "template": "Complétez: 'I ___ a student.'",
                "type": "vocabulaire",
                "concepts": ["Verbe to be"],
                "reponse_index": 1,
                "explications": [
                    "have",
                    "am",
                    "is",
                    "are"
                ]
            }
        ]
    },

    "histoire_geographie": {
        "HIS": [  # Histoire
            {
                "template": "Quel événement marque le début de l'Antiquité?",
                "type": "vocabulaire",
                "concepts": ["Antiquité", "Chronologie"],
                "reponse_index": 1,
                "explications": [
                    "L'invention de l'écriture",
                    "La construction des pyramides d'Égypte",
                    "La chute de l'Empire romain",
                    "La Renaissance"
                ]
            }
        ],
        "GEO": [  # Géographie
            {
                "template": "Qu'est-ce que l'équateur?",
                "type": "vocabulaire",
                "concepts": ["Équateur", "Localisation"],
                "reponse_index": 0,
                "explications": [
                    "Une ligne imaginaire qui divise la Terre en deux hémisphères.",
                    "La frontière entre deux pays.",
                    "Un océan.",
                    "Une montagne."
                ]
            },
            {
                "template": "Quel est le plus grand océan?",
                "type": "vocabulaire",
                "concepts": ["Océans"],
                "reponse_index": 2,
                "explications": [
                    "L'Atlantique",
                    "L'Indien",
                    "Le Pacifique",
                    "L'Arctique"
                ]
            }
        ]
    },

    "sciences_technologie": {
        "SVT": [  # SVT
            {
                "template": "Qu'est-ce qu'une cellule?",
                "type": "vocabulaire",
                "concepts": ["Cellule"],
                "reponse_index": 0,
                "explications": [
                    "La plus petite unité vivante.",
                    "Une partie du cœur.",
                    "Un type de protéine.",
                    "Un organe du corps."
                ]
            },
            {
                "template": "Quel est le rôle des producteurs dans une chaîne alimentaire?",
                "type": "comprehension",
                "concepts": ["Chaîne alimentaire"],
                "reponse_index": 1,
                "explications": [
                    "Manger les autres organismes.",
                    "Produire de l'énergie à partir du soleil (plantes).",
                    "Décomposer la matière morte.",
                    "Polluer l'environnement."
                ]
            }
        ],
        "PC": [  # Physique-Chimie
            {
                "template": "Qu'est-ce qu'une atome?",
                "type": "vocabulaire",
                "concepts": ["Atome"],
                "reponse_index": 2,
                "explications": [
                    "Un type d'énergie.",
                    "Une molécule complexe.",
                    "La plus petite particule d'un élément chimique.",
                    "Un gaz."
                ]
            },
            {
                "template": "À quelle température l'eau bout-elle?",
                "type": "vocabulaire",
                "concepts": ["États de la matière"],
                "reponse_index": 3,
                "explications": [
                    "50°C",
                    "80°C",
                    "90°C",
                    "100°C"
                ]
            }
        ],
        "TECH": [  # Technologie
            {
                "template": "Qu'est-ce qu'un capteur en technologie?",
                "type": "vocabulaire",
                "concepts": ["Capteur"],
                "reponse_index": 1,
                "explications": [
                    "Un moteur qui fait tourner.",
                    "Un dispositif qui détecte des changements (température, lumière, etc.).",
                    "Une source d'énergie.",
                    "Un fil électrique."
                ]
            }
        ]
    }
}

class QCMGenerator:
    def __init__(self):
        self.qcm_data = {}

    def generate_qcm(self, matiere: str, domaine_id: str, domaine_nom: str,
                     competences: List[Dict], concepts: List[str]) -> Dict:
        """Génère un QCM unique basé sur les templates"""

        templates_matiere = QCM_TEMPLATES.get(matiere, {})
        templates_domaine = templates_matiere.get(domaine_id, [])

        if not templates_domaine:
            return None

        template = random.choice(templates_domaine)

        return {
            "id": f"{matiere}_{domaine_id}_{random.randint(1000, 9999)}",
            "matiere": matiere,
            "domaine_id": domaine_id,
            "domaine_nom": domaine_nom,
            "competences_liees": [c.get("titre", "") for c in competences[:2]],
            "concepts_evalues": template.get("concepts", []),
            "type_exercice": template.get("type", "comprehension"),
            "question": template.get("template", ""),
            "options": [
                {"label": "A", "texte": template["explications"][0]},
                {"label": "B", "texte": template["explications"][1]},
                {"label": "C", "texte": template["explications"][2]},
                {"label": "D", "texte": template["explications"][3]}
            ],
            "reponse_correcte": ["A", "B", "C", "D"][template.get("reponse_index", 0)],
            "explication": f"La bonne réponse est {['A', 'B', 'C', 'D'][template.get('reponse_index', 0)]} : {template['explications'][template.get('reponse_index', 0)]}",
            "niveau": "6ème",
            "difficulte": random.choice(["facile", "moyen", "difficile"])
        }

    def generate_all_qcm(self) -> None:
        """Génère les QCM pour tous les fichiers curriculum"""

        print("=" * 70)
        print("ÉTAPE 4 - Génération des QCM")
        print("=" * 70)

        curriculum_files = list(CURRICULUM_DIR.glob("*.json"))
        total_qcm = 0

        for curriculum_file in sorted(curriculum_files):
            print(f"\n📚 Traitement: {curriculum_file.name}")

            with open(curriculum_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            matiere = data.get("matiere", "").lower().replace("-", "_").replace(" ", "_")
            qcm_list = []

            # Génère 5-8 QCM par domaine
            for domaine in data.get("domaines_apprentissage", []):
                domaine_id = domaine.get("id", "")
                domaine_nom = domaine.get("nom", "")
                competences = domaine.get("competences", [])
                concepts = domaine.get("concepts_cles", [])

                nb_qcm = random.randint(5, 8)
                for _ in range(nb_qcm):
                    qcm = self.generate_qcm(matiere, domaine_id, domaine_nom,
                                          competences, concepts)
                    if qcm:
                        qcm_list.append(qcm)

                print(f"   ✅ {domaine_nom}: {nb_qcm} QCM générés")

            # Sauvegarde les QCM
            output_file = OUTPUT_DIR / f"{matiere}_qcm_6eme.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump({"qcm": qcm_list, "total": len(qcm_list)}, f,
                         ensure_ascii=False, indent=2)

            print(f"   📁 Saved: {output_file.name} ({len(qcm_list)} QCM)")
            total_qcm += len(qcm_list)

        print("\n" + "=" * 70)
        print(f"✅ SUCCÈS: {total_qcm} QCM générés pour toutes les matières!")
        print(f"📂 Location: {OUTPUT_DIR}")
        print("=" * 70)

if __name__ == "__main__":
    generator = QCMGenerator()
    generator.generate_all_qcm()
