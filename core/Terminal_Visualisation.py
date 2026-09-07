"""
ce fichier permer d'affiche les resultat du scanne :
"""


# cette fonction permet d'afficher les résultats dans le terminal
def affiches(result):

    print("\n\tla page est accessible....\n")
    print(result["url"])
    print(f"  [+] Status                  : {result['status_code']}")
    print(f"  [+] Server                  : {result['server']}")
    print(f"  [+] Content-Type            : {result['content_type']}")
    print(f"  [+] Cache-Control           : {result['cache_control']}")
    print(f"  [+] X-Powered-By            : {result['x_powered_by']}")
    print(f"  [+] X-Frame-Options         : {result['x_frame_options']}")
    print(f"  [+] X-XSS-Protection        : {result['x_xss_protection']}")
    print(f"  [+] Content-Security-Policy : {result['content_security_policy']}")
    print(f"  [+] content-security-policy-report-only : {result['content_security_policy_report_only']}")
    print(f"  [+] Set-Cookie              : {result['set_cookie']}")
    print("\n")

