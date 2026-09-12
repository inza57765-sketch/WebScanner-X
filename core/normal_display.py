"""
Affichage :
Mode      : Verbose
"""


# cette fonction permet d'afficher les résultats dans le terminal
def affiches(result):

    print("\n\tla page est accessible....\n")
    print(result["url"])

    print("_______________________________")
    print(f"[+] Status                    : {result['status_code']}")
    print(f"[+] Server                    : {result['server']}")

    print(f"[+] Content-Type              : {result['content_type']}")
    print(f"[+] Content-Security-Policy   : {result['content_security_policy']}")
    print(f"[+] Strict-Transport-Security : {result['strict_transport_security']}")
    print(f"[+] X-Frame-Options           : {result['x_frame_options']}")
    print(f"[+] X-XSS-Protection          : {result['x_xss_protection']}")

    print(f"[+] Cache-Control             : {result['cache_control']}")
    print(f"[+] Content-Encoding          : {result['content_encoding']}")
    print(f"[+] Content-Length            : {result['content_length']}")
    print(f"[+] Set-Cookie                : {result['set_cookie']}")

    print(f"[+] Accept-Ranges             : {result['accept_ranges']}")
    print(f"[+] Via                       : {result['via']}")
    print(f"[+] X-Powered-By              : {result['x_powered_by']}")
    print(f"[+] Content-Security-Policy-Report-Only : {result['content_security_policy_report_only']}")
    #print("________________________________________")

    print("\n")
