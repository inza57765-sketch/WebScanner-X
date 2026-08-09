import requests
from datetime import datetime


#url = input("url : ")
url = "http://localhost:8081"

tool_name  = "WebScanner-X"
start_time = datetime.now().strftime("%Y-%m-%d _ %H:%M:%S")

print("\n")
print("|-------------------------------------|")
print(f"|Start     : {start_time}    |")
print(f"|Programme : {tool_name}             |")
print("|-------------------------------------|")
print("|Dev       : @Cyber-Tchak             |")
print("|GitHub    : inza57765-sketch         |")
print("|-------------------------------------|")
print("\n\n")


head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0;  Win64; x64) AppleWebKit/537.36"
}

try:

    if url.startswith("https://") or url.startswith("http://"):
        response                = requests.get(url, headers=head)
        status_code             = response.status_code
        server                  = response.headers.get("Server",                  "Non indiqué")
        x_powered_by            = response.headers.get("X-Powered-By",            "Non indiqué")
        content_security_policy = response.headers.get("Content-Security-Policy", "Absent")
        x_frame_options         = response.headers.get("X-Frame-Options",         "Absent")
        set_cookies             = response.headers.get("Set-Cookie",              "Absent")
        content_type            = response.headers.get("Content-Type",            "Non indiqué")

        if response.status_code == 200:
            print("\n\t\t\tla page est accessible....\n")
            print("="*59)
            print(url)
            print("="*59)
            print(f"              Status                  : {status_code}")
            print(f"              Server                  : {server}")
            print(f"              X-Powered-By            : {x_powered_by}")
            print(f"              Content-Security-Policy : {content_security_policy}")
            print(f"              X-Frame-Options         : {x_frame_options}")
            print(f"              Set-Cookie              : {set_cookies}")
            print(f"              Content-Type            : {content_type}")
            print("-"*59)
            print("\n")

        affiche = {
        }

    else:
        print("\nVerifie le protocol")



except requests.exceptions.ConnectionError:
    print("\nimpossible de se connecté au site.")

    print("-"*59)
    print("""
Voici quelques conseils :

      1. Désactivez le mode Avion.
      2. Activez les données mobiles ou le réseau Wi-Fi.
      3. Vérifiez le signal dans votre zone.

ERR_INTERNET_DISCONNECTED
    """)
    print("-"*59)
    print("\n")

except requests.exceptions.Timeout:
    print("\nle site as mis trop de temps à repondre.")
    print("Timeout.\n")

except KeyboardInterrupt:
    print("\nInterruption clavier.")
