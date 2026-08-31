import os
import json
import subprocess as sub
from datetime import datetime


def setting_func(result):

    core    = os.path.dirname(os.path.abspath(__file__))
    projet  = os.path.dirname(core)
    fichier = os.path.join(projet, "configs", "settings.json")

    with open(fichier, "r") as configs:
        config = json.load(configs)

    clear     = config["ScreenClean"]
    set_logs  = config["generate_Logs"]


    if clear == True:
        sub.run(["clear"])

    elif set_logs == True:
        log = open("logs", "a", encoding="utf-8")

        heure = datetime.now().strftime("%H:%M:%S")
        date  = datetime.now().strftime("%Y-%m-d")
        url   = result["url"]

        log.write(f"[heure : {heure}]")
        log.write(f"[date  : {date}]")
        log.write(f"url    : {url}")




