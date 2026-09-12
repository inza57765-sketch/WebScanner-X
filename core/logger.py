import os
import subprocess as sub
from   datetime import datetime

"""
Enregistrement :
Module         : logger
"""
def logger_run(result):
        heure = datetime.now().strftime("%H:%M:%S")
        date  = datetime.now().strftime("%Y-%m-%d")

        registre_parent = ".WebScanner-X_Logs"
        url       = result["url"]
        url_split = url.split("/")
        domaine   = url_split[2]
        file_log  = f"{registre_parent}/{domaine}.log"


        if not os.path.exists(registre_parent):
            os.mkdir(registre_parent)

        if not os.path.exists(file_log):
            sub.run(["touch", file_log])

        log = open(file_log, "a", encoding="utf-8")

        heure = datetime.now().strftime("%H:%M:%S")
        date  = datetime.now().strftime("%Y-%m-%d")

        log.write(f"\n[heure : {heure}]")
        log.write(f"\n[date  : {date}]")
        log.write(f"\nUrl    : {result['url']}")
        log.write(f"\nStatus : {result['status_code']}")
        log.write(f"\nTemps  : {result['response_time']}")

        log.write("\n\n\n")
