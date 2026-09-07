from pathlib import Path

def cli_readme():
    try:
        readme = Path(__file__).resolve().parent / "README.md"

        with readme.open("r", encoding="utf-8") as fichier:
            print("\nWebScanner-X : README")
            print(fichier.read())
            print("\n")

    except FileNotFoundError:
        print("\nWebScanner-X : README introuvable.")

