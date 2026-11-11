#!/usr/bin/env python3
"""
Script de téléchargement des PDFs de programmes Éduscol pour la 6ème
Étape 3: Extraction du contenu
"""

import os
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
OUTPUT_DIR = Path("./data/pdfs_programmes")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Liste des PDFs à télécharger (Étape 2 - URLs confirmées)
PDFS_TO_DOWNLOAD = {
    "francais": {
        "url": "https://www.education.gouv.fr/sites/default/files/programme-de-francais-pour-le-cycle-3-439824.pdf",
        "filename": "01_FRANCAIS_cycle3.pdf",
        "bo": "BO n° 16 du 17 avril 2025"
    },
    "mathematiques": {
        "url": "https://www.education.gouv.fr/sites/default/files/programme-de-math-matiques-pour-le-cycle-3-439827.pdf",
        "filename": "02_MATHEMATIQUES_cycle3.pdf",
        "bo": "BO n° 16 du 17 avril 2025"
    },
    "histoire_geographie": {
        "url": "https://www.education.gouv.fr/sites/default/files/programme-d-histoire-geographie-pour-le-cycle-3-439826.pdf",
        "filename": "04_HISTOIRE_GEOGRAPHIE_cycle3.pdf",
        "bo": "BO n° 31 du 30 juillet 2020"
    },
    "langues_vivantes": {
        "url": "https://www.education.gouv.fr/sites/default/files/programme-langues-vivantes-etrangeres-cycle-3-439823.pdf",
        "filename": "03_LANGUES_VIVANTES_cycle3.pdf",
        "bo": "BO n° 22 du 29 mai 2025"
    },
    "sciences_technologie": {
        "url": "https://www.education.gouv.fr/sites/default/files/programme-sciences-technologie-cycle-3-439828.pdf",
        "filename": "05_SCIENCES_TECHNOLOGIE_cycle3.pdf",
        "bo": "BO n° 25 du 22 juin 2023"
    }
}

# Headers pour la requête (simule un navigateur)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def download_pdf(url, filepath, matiere):
    """Télécharge un PDF et le sauvegarde localement"""
    try:
        print(f"📥 Téléchargement: {matiere}...")
        response = requests.get(url, headers=HEADERS, timeout=30, verify=False)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            f.write(response.content)

        file_size_mb = os.path.getsize(filepath) / (1024 * 1024)
        print(f"✅ {matiere}: {filepath} ({file_size_mb:.2f} MB)")
        return True
    except Exception as e:
        print(f"❌ Erreur pour {matiere}: {str(e)}")
        return False

def download_all_pdfs():
    """Télécharge tous les PDFs des programmes"""
    print("=" * 60)
    print("ÉTAPE 3 - Téléchargement des PDFs de programmes")
    print("=" * 60)
    print(f"\nDossier de destination: {OUTPUT_DIR.absolute()}\n")

    success_count = 0
    total_count = len(PDFS_TO_DOWNLOAD)

    for matiere, info in PDFS_TO_DOWNLOAD.items():
        filepath = OUTPUT_DIR / info["filename"]

        # Affiche l'info
        print(f"\n📚 {info['filename'].split('_')[1]}")
        print(f"   BO: {info['bo']}")
        print(f"   URL: {info['url'][:70]}...")

        # Télécharge
        if download_pdf(info["url"], filepath, matiere):
            success_count += 1

        # Petit délai entre les téléchargements pour ne pas surcharger le serveur
        time.sleep(1)

    # Résumé
    print("\n" + "=" * 60)
    print(f"Résumé: {success_count}/{total_count} PDFs téléchargés avec succès")
    print("=" * 60)

    return success_count == total_count

if __name__ == "__main__":
    success = download_all_pdfs()
    exit(0 if success else 1)
