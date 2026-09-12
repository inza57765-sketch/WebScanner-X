import socket


def dns_trad(domaine):
    try:
        domaine_ip = socket.gethostbyname(domaine)
        print(f"""
─────────┬────────────────
domaine  │ {domaine}
IP       │ {domaine_ip}
─────────┴────────────────
        """)


    except socket.gaierror:
        print("\n")
        print("WebScanner-X : Impossible résoud ce domaine.") #d'établir une connexion avec la cible.
        print("\n")

    except UnicodeEncodeError:
        print("\n")
        print("WebScanner-X : Caractère invalide")
        print("\n")

    except KeyboardInterrupt:
        print("\n")
        print("WebScanner-X : Interruption Clavier")
        print("\n")

    except Exception as erreur:
        print("\n")
        print(f"WebScanner-X : {erreur}")
