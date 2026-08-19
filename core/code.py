

#Explications du rôle de ce fichier
"""
ce fichier est le cœur de l'outil
sais lui qui met en place l'ordre donné par le fichier d'orchestre
"""


#Importations des bibliothèques et modules
######################################################|
import requests                                      #|
import subprocess as sub                             #|
from .banner import Banner                           #|
from .Terminal_Visualisation import affiches         #|
from .couleurs import BLEU, JAUNE, RESET, ROUGE, VERT#|
######################################################|

#Fontions pour importer le code source facilement
def Source_Code(base_url):
    Banner()


    #Definire un  User-Agent
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0;  Win64; x64) AppleWebKit/537.36"
    }


    try:
        response                = requests.get(base_url, headers=headers, timeout=5)
        status_code             = response.status_code
        server                  = response.headers.get(f"Server",                  f"{ROUGE}Non indiqué{RESET}")
        x_powered_by            = response.headers.get(f"X-Powered-By",            f"{VERT}Non indiqué{RESET} ")
        content_security_policy = response.headers.get(f"Content-Security-Policy", f"{ROUGE}Absent{RESET}     ")
        x_frame_options         = response.headers.get(f"X-Frame-Options",         f"{ROUGE}Absent{RESET}     ")
        set_cookies             = response.headers.get(f"Set-Cookie",              f"{VERT}Absent{RESET}      ")
        content_type            = response.headers.get(f"Content-Type",            f"{ROUGE}Non indiqué{RESET}")

        result = {
            "url":base_url,
            "response":response,
            "status_code":status_code,
            "server":server,
            "x_powered_by":x_powered_by,
            "content_security_policy":content_security_policy,
            "x_frame_options":x_frame_options,
            "set_cookie":set_cookies,
            "content_type":content_type
        }


        if response.status_code == 200:
            affiches(result)



    except requests.exceptions.ConnectionError:
        print(f"\n{ROUGE}Impossible de se connecté au site.{RESET}")

        print("-"*59)
        print(f"""{JAUNE}
    Voici quelques conseils :

        1. Désactivez le mode Avion.
        2. Activez les données mobiles ou le réseau Wi-Fi.
        3. Vérifiez le signal dans votre zone.
        4. Ou la page est hors service.

    REQUESTS_CONNECT_EROR
        {RESET}""")
        print("-"*59)
        print("\n")

    #Géré les exceptions
    ########################################################################|
    except requests.exceptions.InvalidURL:                                 #|
        print("\nErreur : Url invalide.")                                  #|
    except requests.exceptions.MissingSchema:                              #|
        print("\nErreur : Url invalide.")                                  #|
    except requests.exceptions.InvalidSchema:                              #|
        print("\nErreur : Url invalide.")                                  #|
    except requests.exceptions.Timeout:                                    #|
        print(f"\n{JAUNE}Le site as mis trop de temps à repondre.{RESET}") #|
        print(f"{BLEU}Timeout{RESET}.\n")                                  #|
    except FileNotFoundError:                                              #|
        print(f"\n{ROUGE}Erreur : Fichier introuvable.{RESET}")            #|
    except FileExistsError:                                               #|
        print("\nErreur : Fichier inexistant.")                           #|
    except KeyboardInterrupt:                                              #|
        print(f"\n{BLEU}Interruption clavier.{RESET}")                     #|
    ########################################################################|
