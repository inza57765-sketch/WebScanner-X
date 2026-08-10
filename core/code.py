
"""
ce fichier est le cœur de l'outil
sais lui qui met en place l'ordre donné par le fichier d'orchestre
"""

import requests
from banner import Banner
from Terminal_Visualisation import affiches
from response_analyse import response_analyse_run


#url = input("url : ")
url = "http://localhost:8081"


Banner()

head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0;  Win64; x64) AppleWebKit/537.36"
}

try:
    response                = requests.get(url, headers=head)
    status_code             = response.status_code
    server                  = response.headers.get("Server",                  "Non indiqué")
    x_powered_by            = response.headers.get("X-Powered-By",            "Non indiqué")
    content_security_policy = response.headers.get("Content-Security-Policy", "Absent")
    x_frame_options         = response.headers.get("X-Frame-Options",         "Absent")
    set_cookies             = response.headers.get("Set-Cookie",              "Absent")
    content_type            = response.headers.get("Content-Type",            "Non indiqué")

    result = {
        "url":url,
        "response":response,
        "status_code":status_code,
        "server":server,
        "x_powered_by":x_powered_by,
        "content_security_policy":content_security_policy,
        "x_frame_options":x_frame_options,
        "set_cookie":set_cookies,
        "content_type":content_type
    }

    response_analyse_run(result)        


except requests.exceptions.ConnectionError:
    print("\nImpossible de se connecté au site.")

    print("-"*59)
    print("""
Voici quelques conseils :

      1. Désactivez le mode Avion.
      2. Activez les données mobiles ou le réseau Wi-Fi.
      3. Vérifiez le signal dans votre zone.

REQUESTS_CONNECT_EROR
    """)
    print("-"*59)
    print("\n")

except requests.exceptions.Timeout:
    print("\nle site as mis trop de temps à repondre.")
    print("Timeout.\n")

except KeyboardInterrupt:
    print("\nInterruption clavier.")
