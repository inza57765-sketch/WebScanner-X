#!/usr/bin/env python3


# Importations des bibliothèques et modules
import time
import requests
import subprocess as sub
from . import (
        Banner,
        headers_func,
        affiches,
        logger_run,
        not_found,
        BLEU,
        JAUNE,
        RESET,
        ROUGE,
        VERT
)




# Fontions pour importer facilement le code source.
def Source_Code(base_url):
    Banner()


    # Definire un  User-Agent
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0;  Win64; x64) AppleWebKit/537.36"
    }


    try:
        start         = time.perf_counter()
        response      = requests.get(base_url, headers=headers, timeout=5)
        end           = time.perf_counter()
        response_time = end - start



        status_code             = response.status_code
        server                  = response.headers.get(f"Server",                  f"{ROUGE}Non indiqué{RESET}")

        content_type            = response.headers.get("Content-Type",             f"{ROUGE}Non indiqué{RESET}")
        cache_control           = response.headers.get("Cache-Control",            f"{ROUGE}Non indiqué{RESET}")
        accept_ranges           = response.headers.get("Accept-Ranges",                      f"{ROUGE}Non indiqué{RESET}")

        via                     = response.headers.get("Via",                      f"{ROUGE}Non indiqué{RESET}")

        x_powered_by            = response.headers.get("X-Powered-By",             f"{VERT}Non  indiqué{RESET}")
        x_frame_options         = response.headers.get("X-Frame-Options",          f"{ROUGE}Absent{RESET}")
        x_xss_protection        = response.headers.get("X-XSS-Protection",         f"{ROUGE}Non indiqué{RESET}")
        content_security_policy = response.headers.get("Content-Security-Policy",  f"{ROUGE}Absent{RESET}")

        content_security_policy_report_only = response.headers.get("Content-Security-Policy-Report-Only", f"{ROUGE}Non indiqué{RESET}")
        strict_transport_security           = response.headers.get("Strict-Transport-Security",           f"{ROUGE}Non indiqué{RESET}")

        set_cookies             = response.headers.get(f"Set-Cookie",                                     f"{VERT}Absent{RESET}")
        content_encoding        = response.headers.get("Content-Encoding",         f"{ROUGE}Non indiqué{RESET}")
        content_length          = response.headers.get("Content-Length",               f"{ROUGE}Non indiqué{RESET}")


        result = {

            "url": base_url,
            "status_code": status_code,
            "server": server,


            "content_type": content_type,
            "content_security_policy": content_security_policy,
            "strict_transport_security": strict_transport_security,
            "x_frame_options": x_frame_options,
            "x_xss_protection": x_xss_protection,


            "cache_control": cache_control,
            "content_encoding": content_encoding,
            "content_length": content_length,
            "set_cookie": set_cookies,


            "accept_ranges": accept_ranges,
            "via": via,
            "x_powered_by": x_powered_by,
            "content_security_policy_report_only": content_security_policy_report_only,


            "response_time":f"{response_time:.2f}s"
        }





        if response.status_code == 200:

            #affiches(result)
            headers_func(result)
            print(f"Temps : {response_time:.2f}s")
            logger_run(result)



        elif status_code == 404:
            not_found(result)
            print(f"Temps  : {response_time:.2f}s")
            logger_run(result)






    # Géré les exceptions
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
        print(f"\n{VERT}WebScanner-X{RESET} : Url invalide.")



    except requests.exceptions.Timeout:
        print(f"\n{VERT}WebScanner-X{RESET} : {JAUNE}La cible n'a pas répondu dans le délai imparti.{RESET}")
        print(f"{BLEU}Timeout{RESET}.\n")

    except FileNotFoundError:
        print(f"\n{VERT}WebScanner-X{RESET} : {ROUGE}Fichier introuvable.{RESET}")

    except KeyboardInterrupt:
        print(f"\n{VERT}WebScanner-X{RESET} : {BLEU}Interruption clavier.{RESET}")
