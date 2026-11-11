#!/usr/bin/env python3
"""
Script simplifié de génération des QCM
Étape 4: Génération d'exercices QCM - Version 2
"""

import json
from pathlib import Path
from typing import List, Dict
import random

CURRICULUM_DIR = Path("./data/curricula")
OUTPUT_DIR = Path("./data/exercices/qcm")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Questions pré-définies par sujet
QUESTIONS = {
    "Français": [
        {"Q": "Qu'est-ce qu'un verbe?", "A": ["Action ou état", "Nom du personnage", "Lieu du récit", "Temps de l'histoire"], "R": 0, "C": ["Verbe", "Grammaire"]},
        {"Q": "Quel est le sujet de 'Le chat dort'?", "A": ["Le chat", "dort", "chat", "Le"], "R": 0, "C": ["Sujet", "Phrase"]},
        {"Q": "Qu'est-ce qu'un texte narratif?", "A": ["Qui raconte une histoire", "Qui décrit un lieu", "Qui donne une opinion", "Qui explique"], "R": 0, "C": ["Texte narratif", "Lecture"]},
        {"Q": "Comment s'appelle le héros?", "A": ["Personnage principal", "Auteur", "Lecteur", "Critique"], "R": 0, "C": ["Héros", "Littérature"]},
        {"Q": "Qu'est-ce qu'un adjectif?", "A": ["Mot qui modifie le nom", "Mot qui exprime l'action", "Mot invariable", "Mot de transition"], "R": 0, "C": ["Adjectif", "Grammaire"]},
        {"Q": "Quel est le rôle de la ponctuation?", "A": ["Clarifier le sens du texte", "Augmenter la longueur", "Changer les mots", "Ajouter des images"], "R": 0, "C": ["Ponctuation", "Écriture"]},
        {"Q": "Qu'est-ce qu'une métaphore?", "A": ["Comparaison sans 'comme'", "Répétition de sons", "Énumération", "Description détaillée"], "R": 0, "C": ["Figure de style", "Littérature"]},
    ],
    "Mathématiques": [
        {"Q": "Combien de côtés a un triangle?", "A": ["3", "4", "5", "6"], "R": 0, "C": ["Triangle", "Géométrie"]},
        {"Q": "Qu'est-ce qu'un nombre décimal?", "A": ["Nombre avec virgule", "Nombre négatif", "Nombre entier", "Nombre pair"], "R": 0, "C": ["Décimal", "Nombres"]},
        {"Q": "Quel est le résultat de 5 × 3?", "A": ["15", "8", "2", "12"], "R": 0, "C": ["Multiplication", "Calcul"]},
        {"Q": "Qu'est-ce qu'une fraction?", "A": ["Partie d'un tout", "Un nombre entier", "Une division", "Un pourcentage"], "R": 0, "C": ["Fraction", "Nombres"]},
        {"Q": "Combien de mètres dans 1 km?", "A": ["1000", "100", "10", "500"], "R": 0, "C": ["Longueur", "Mesure"]},
        {"Q": "Qu'est-ce qu'une symétrie?", "A": ["Correspondance exacte", "Rotation", "Agrandissement", "Déplacement"], "R": 0, "C": ["Symétrie", "Géométrie"]},
        {"Q": "Quel est le périmètre d'un carré de 5 cm?", "A": ["20 cm", "25 cm", "10 cm", "15 cm"], "R": 0, "C": ["Périmètre", "Géométrie"]},
    ],
    "Anglais": [
        {"Q": "How do you say 'Hello'?", "A": ["Hello", "Goodbye", "Thank you", "Please"], "R": 0, "C": ["Greetings", "Vocabulaire"]},
        {"Q": "What is 'I am'?", "A": ["Je suis", "Tu es", "Il est", "Elle est"], "R": 0, "C": ["Verbe to be", "Grammaire"]},
        {"Q": "Complétez: 'My name ___ John'", "A": ["is", "am", "are", "be"], "R": 0, "C": ["To be", "Grammaire"]},
        {"Q": "How do you say 'Thank you'?", "A": ["Thank you", "You're welcome", "Sorry", "Excuse me"], "R": 0, "C": ["Politeness", "Vocabulaire"]},
        {"Q": "What is the color of the sky?", "A": ["Blue", "Red", "Green", "Yellow"], "R": 0, "C": ["Colors", "Vocabulaire"]},
        {"Q": "Translate 'chat' to English", "A": ["Cat", "Dog", "Bird", "Fish"], "R": 0, "C": ["Animals", "Vocabulaire"]},
    ],
    "Histoire-Géographie": [
        {"Q": "Qu'est-ce que l'équateur?", "A": ["Ligne qui divise la Terre", "Frontière d'un pays", "Océan", "Montagne"], "R": 0, "C": ["Équateur", "Géographie"]},
        {"Q": "Quel est le plus grand océan?", "A": ["Pacifique", "Atlantique", "Indien", "Arctique"], "R": 0, "C": ["Océans", "Géographie"]},
        {"Q": "Combien de continents?", "A": ["7", "5", "6", "8"], "R": 0, "C": ["Continents", "Géographie"]},
        {"Q": "Quelle est la capitale de la France?", "A": ["Paris", "Lyon", "Marseille", "Toulouse"], "R": 0, "C": ["France", "Géographie"]},
        {"Q": "Quand la Préhistoire a-t-elle commencé?", "A": ["Avant l'écriture", "Après l'écriture", "À l'an 0", "En 1000"], "R": 0, "C": ["Préhistoire", "Histoire"]},
        {"Q": "Qui a exploré l'Amérique?", "A": ["Christophe Colomb", "Magellan", "Marco Polo", "Vasco de Gama"], "R": 0, "C": ["Exploration", "Histoire"]},
    ],
    "Sciences et Technologie": [
        {"Q": "Qu'est-ce qu'une cellule?", "A": ["Unité vivante", "Partie de l'atome", "Type de protéine", "Organe du corps"], "R": 0, "C": ["Cellule", "SVT"]},
        {"Q": "À quelle température l'eau bout?", "A": ["100°C", "50°C", "0°C", "150°C"], "R": 0, "C": ["États de la matière", "Physique"]},
        {"Q": "Qu'est-ce qu'un atome?", "A": ["Plus petite particule", "Molécule complexe", "Type d'énergie", "Gaz"], "R": 0, "C": ["Atome", "Chimie"]},
        {"Q": "Quel est le rôle de la photosynthèse?", "A": ["Produire du glucose", "Créer de l'oxygène", "Manger la lumière", "Transporter l'eau"], "R": 0, "C": ["Photosynthèse", "SVT"]},
        {"Q": "Qu'est-ce qu'un capteur?", "A": ["Détecte les changements", "Moteur", "Source d'énergie", "Fil électrique"], "R": 0, "C": ["Capteur", "Technologie"]},
        {"Q": "Combien de membres l'homme a-t-il?", "A": ["4", "2", "6", "3"], "R": 0, "C": ["Anatomie", "SVT"]},
    ]
}

def generate_qcm_for_subject(subject, questions):
    """Génère les QCM pour une matière"""
    qcm_list = []

    for i, q_data in enumerate(questions):
        qcm = {
            "id": f"{subject}_{i:03d}",
            "matiere": subject,
            "question": q_data["Q"],
            "options": [
                {"label": "A", "texte": q_data["A"][0]},
                {"label": "B", "texte": q_data["A"][1]},
                {"label": "C", "texte": q_data["A"][2]},
                {"label": "D", "texte": q_data["A"][3]}
            ],
            "reponse_correcte": ["A", "B", "C", "D"][q_data["R"]],
            "explication": f"La réponse est {['A', 'B', 'C', 'D'][q_data['R']]}: {q_data['A'][q_data['R']]}",
            "concepts": q_data["C"],
            "niveau": "6ème",
            "type_exercice": "QCM"
        }
        qcm_list.append(qcm)

    return qcm_list

def main():
    print("=" * 70)
    print("ÉTAPE 4 - Génération des QCM (Version 2)")
    print("=" * 70)

    total_qcm = 0

    for subject, questions in QUESTIONS.items():
        print(f"\n📚 {subject}")

        qcm_list = generate_qcm_for_subject(subject, questions)

        # Génère le nom du fichier
        filename = subject.lower().replace("-", "").replace(" ", "_") + "_qcm_6eme.json"
        filepath = OUTPUT_DIR / filename

        # Sauvegarde
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                "subject": subject,
                "niveau": "6ème",
                "total": len(qcm_list),
                "qcm": qcm_list
            }, f, ensure_ascii=False, indent=2)

        print(f"   ✅ {len(qcm_list)} QCM générés")
        print(f"   📁 {filename}")
        total_qcm += len(qcm_list)

    print("\n" + "=" * 70)
    print(f"✅ SUCCÈS: {total_qcm} QCM générés!")
    print(f"📂 Location: {OUTPUT_DIR}")
    print("=" * 70)

if __name__ == "__main__":
    main()
