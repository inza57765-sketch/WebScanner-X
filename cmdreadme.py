from pathlib import Path

def cli_readme():
    try:
        readme = Path(__file__).resolve().parent / "README.md"

        with readme.open("r", encoding="utf-8") as fichier:
            print("\n")
            print("WebScanner-X : README")
            print(fichier.read())

    except FileNotFoundError:
        print("WebScanner-X : README introuvable.")

