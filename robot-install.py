#!/usr/bin/env python3

import time
import subprocess as sub
from datetime import datetime
from core.couleurs import INIT, RESET, VERT, LUMINEUX, JAUNE, ROUGE


version = "v0.1"
heure   = datetime.now().strftime("%H:%M:%S")
date    = datetime.now().strftime("%Y-%m-%d")

print("\n")
print(f"{LUMINEUX}robot-install{RESET} : {VERT}{version}{RESET}")
print(f"Heure : {heure}")
print(f"Date  : {date}")
print("\n")
time.sleep(1)

install_fichier = "install.sh"
step            = [f"{LUMINEUX}robot-install{RESET} : {VERT}[+]{RESET} lancement"]

print("\n")
for s in step:
      print(s, end="", flush=True)
      for i in range(4):
           print(f"{VERT}.{RESET}", end="", flush=True)
           time.sleep(0.9)
      print("✓.")
print(f"{ROUGE}+{RESET}{JAUNE}--------------------{RESET}{VERT}INSTALLATIONS{RESET}{JAUNE}------------------{RESET}{ROUGE}+{RESET}")
time.sleep(1)


print("\n")
fichier_exec = sub.run(["chmod", "+x", install_fichier])
if fichier_exec.returncode !=0:
     print(f"{LUMINEUX}robot-install{VERT} : {ROUGE}[-]{RESET} Operation [!=0].")
     time.sleep(1)
     print(f"{LUMINEUX}robot-install{RESET} : {ROUGE}[-]{RESET} fichier/{install_fichier} >non-executable.\n")
else:
     print(f"{LUMINEUX}robot-install{RESET} : {VERT}[+]{RESET} fichier/{install_fichier}  >executable   ✓.\n")



install_exec = sub.run(["bash" , install_fichier])
if install_exec.returncode !=0:
     print(f"\n{LUMINEUX}robot-install{RESET} : {ROUGE}[-]{RESET} Operation [!=0].")
     time.sleep(1)
     print(f"{LUMINEUX}robot-install{RESET} : {ROUGE}[-]{RESET} installation des paquets échoué.")
else:
     print(f"{LUMINEUX}robot-install{RESET} : {VERT}[+]{RESET} installation des paquets terminé.")
print("\n")

