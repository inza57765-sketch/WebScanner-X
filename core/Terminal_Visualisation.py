def affiches(affiche):


    
    print("\n\t\t\tla page est accessible....\n")
    print("="*59)
    print(affiche["url"])
    print("="*59)
    print(f"              Status                  : {affiche["status_code"]}")
    print(f"              Server                  : {affiche["server"]}")
    print(f"              X-Powered-By            : {affiche["x_powered_by"]}")
    print(f"              Content-Security-Policy : {affiche["content_security_policy"]}")
    print(f"              X-Frame-Options         : {affiche["x_frame_options"]}")
    print(f"              Set-Cookie              : {affiche["set_cookies"]}")
    print(f"              Content-Type            : {affiche["content_type"]}")
    print("-"*59)
    print("\n")

