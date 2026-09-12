def outil_aide():
    try:
        fichier_aide = "help.txt"
        with open(fichier_aide, "r", encoding="utf-8") as aide:
            read_help = aide.read()
            print("\nWebScanner-X : aide")
            print(read_help)
            print("\n")

    except FileNotFoundError:
        print("WebScanner-X : fichier d'aide introuvable.")
