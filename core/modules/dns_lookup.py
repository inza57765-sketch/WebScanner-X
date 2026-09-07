import socket


def dns_trad(domaine):
    try:
        domaine_ip = socket.gethostbyname(domaine)
        print(f"\ndomaine : {domaine}")
        print(f"IP      : {domaine_ip}")


    except socket.gaierror:
        print("\n")
        print("WebScanner-X : Impossible d'établir une connexion avec la cible.")
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
