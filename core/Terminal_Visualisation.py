
"""
ce fichier est l'afficheur des resultats
"""


# cette fonction permet de visualisé le résultat final
def affiches(result):

    print("\n\t\t\tla page est accessible....\n")
    print("="*59)
    print(result["url"])
    print("="*59)
    print(f"              Status                  : {result["status_code"]}")
    print(f"              Server                  : {result["server"]}")
    print(f"              X-Powered-By            : {result["x_powered_by"]}")
    print(f"              Content-Security-Policy : {result["content_security_policy"]}")
    print(f"              X-Frame-Options         : {result["x_frame_options"]}")
    print(f"              Set-Cookie              : {result["set_cookie"]}")
    print(f"              Content-Type            : {result["content_type"]}")
    print("-"*59)
    print("\n")

