import os
import subprocess as sub
from datetime import datetime


date = datetime.now().strftime("%H:%M:%S")

fichier_log = "logs/{date}.log"

def logger_run(result):
#    fichier_log = f"logs/{result["url"]}{date}.log"

    if not os.path.exists(fichier_log):
        os.mkdir("logs")
        sub.run(["touch", f"{fichier_log}"])


    with open(fichier_log, "a", encoding="utf-8") as logs:

        logs.write("="*59)
        logs.write(f"\nurl {result["url"]}\n")
        logs.write("="*59)
        logs.write(f"\nStatus                  : {result["status_code"]}")
        logs.write(f"\nServer                  : {result["server"]}")
        logs.write(f"\nX-Powered-By            : {result["x_powered_by"]}")
        logs.write(f"\nContent-Security-Policy : {result["content_security_policy"]}")
        logs.write(f"\nX-Frame-Options         : {result["x_frame_options"]}")
        logs.write(f"\nSet-Cookie              : {result["set_cookie"]}")
        logs.write(f"\nSet-Cookie              : {result["content_type"]}\n")
        logs.write("-"*59)
        logs.write("\n")
