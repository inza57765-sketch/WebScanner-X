
"""
ce fichier est hors service pour le moment 
raison d'amelioration
"""
"""
                       
head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0;  Win64; x64) AppleWebKit/537.36"
}   

def analyse_run():
        response                = requests.get(url, headers=head)
        status_code             = response.status_code
        server                  = response.headers.get("Server",                  "Non indiqué")
        x_powered_by            = response.headers.get("X-Powered-By",            "Non indiqué")
        content_security_policy = response.headers.get("Content-Security-Policy", "Absent")
        x_frame_options         = response.headers.get("X-Frame-Options",         "Absent")
        set_cookies             = response.headers.get("Set-Cookie",              "Absent")
        content_type            = response.headers.get("Content-Type",            "Non indiqué")

"""