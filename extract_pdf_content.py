#!/usr/bin/env python3
"""
Extrait le contenu réel du PDF de Mathématiques
"""

import PyPDF2
from pathlib import Path

pdf_path = Path("./data/pdfs_programmes/02_MATHEMATIQUES_cycle3.pdf")

print("=" * 70)
print("EXTRACTION DU CONTENU DU PDF MATHÉMATIQUES")
print("=" * 70)

if not pdf_path.exists():
    print(f"❌ Fichier non trouvé: {pdf_path}")
    print("\nPDFs disponibles:")
    pdfs = list(Path("./data/pdfs_programmes").glob("*.pdf"))
    for pdf in pdfs:
        print(f"  - {pdf.name} ({pdf.stat().st_size / 1024:.1f} KB)")
else:
    print(f"\n✅ Fichier trouvé: {pdf_path.name}")
    print(f"   Taille: {pdf_path.stat().st_size / (1024*1024):.2f} MB")

    try:
        with open(pdf_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            num_pages = len(pdf_reader.pages)
            print(f"   Pages: {num_pages}")

            print("\n📖 EXTRACTION DU CONTENU (première page):\n")
            print("-" * 70)

            # Extrait le texte de la première page
            first_page = pdf_reader.pages[0]
            text = first_page.extract_text()

            # Affiche les 1000 premiers caractères
            print(text[:1500])
            print("\n" + "-" * 70)
            print(f"\n✅ Extraction réussie! Contenu disponible.")

    except Exception as e:
        print(f"❌ Erreur lors de la lecture: {e}")
        print("\n💡 Solution: Installer PyPDF2")
        print("   Commande: pip install PyPDF2")
