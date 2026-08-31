
#!/usr/bin/env python3


#Importations des bibliothèques et modules
"""
import   requests
import   subprocess as sub
from .   import Banner
from .   import headers_func
from .   import affiches
from .   import BLEU, JAUNE, RESET, ROUGE, VERT
"""

import requests
import subprocess as sub
from . import (
        Banner,
        headers_func,
        affiches,
        BLEU,
        JAUNE,
        RESET,
        ROUGE,
        VERT
)


# Fontions pour importer le code source facilement
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
        content_type            = response.headers.get(f"Content-Type",            f"{ROUGE}Non indiqué{RESET}")
        cache_control           = response.headers.get("Cache-Control",            f"{ROUGE}Non indiqué{RESET}")
        x_powered_by            = response.headers.get(f"X-Powered-By",            f"{VERT}Non indiqué{RESET} ")
        x_frame_options         = response.headers.get(f"X-Frame-Options",         f"{ROUGE}Absent{RESET}")
        x_xss_protection        = response.headers.get("X-XSS-Protection",         f"{ROUGE}Non indiqué{RESET}")
        content_security_policy = response.headers.get(f"Content-Security-Policy", f"{ROUGE}Absent{RESET}")
        content_security_policy_report_only = response.headers.get("Content-Security-Policy-Report-Only", f"{ROUGE}Non indiqué{RESET}")
        set_cookies             = response.headers.get(f"Set-Cookie",                                     f"{VERT}Absent{RESET}")
        #i = response.headers.get("Strict-Transport-Security", "no")

        result = {
            "url":base_url,
            "status_code":status_code,
            "server":server,
            "content_type":content_type,
            "cache_control":cache_control,
            "x_powered_by":x_powered_by,
            "x_frame_options":x_frame_options,
            "x_xss_protection":x_xss_protection,
            "content_security_policy":content_security_policy,
            "content_security_policy_report_only":content_security_policy_report_only,
            "set_cookie":set_cookies
        }


        if response.status_code == 200:
            #affiches(result)
            headers_func(result)



    #Géré les exceptions
    except requests.exceptions.ConnectionError:
        print(f"""{JAUNE}
{ROUGE}Impossible d'établir une connexion avec la cible.{RESET}
{JAUNE}
------------------------------------------------
    Vérifiez notamment :
    ____________________

        1. Votre connexion Internet.
        2. L'adresse URL saisie.
        3. La résolution DNS du domaine.

    Type d'erreur :
        REQUESTS_CONNECTION_ERROR
------------------------------------------------

        {RESET}""")
        print("\n")


    except (
        requests.exceptions.InvalidSchema,
        requests.exceptions.MissingSchema,
        requests.exceptions.InvalidURL
    ):
        print("\nUrl invalide.")



    except requests.exceptions.Timeout:
        print(f"\n{JAUNE}La cible n'a pas répondu dans le délai imparti.{RESET}")
        print(f"{BLEU}Timeout{RESET}.\n")

    except FileNotFoundError:
        print(f"\n{ROUGE}Fichier introuvable.{RESET}")

    except KeyboardInterrupt:
        print(f"\n{BLEU}Interruption clavier.{RESET}")
