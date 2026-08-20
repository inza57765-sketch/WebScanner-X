
from datetime import datetime
from .couleurs import BLEU, INIT, JAUNE, LUMINEUX, RESET, ROUGE, VERT
"""
ce fichier gerèr le bannere de l'outil
"""

# cette fonction donne une visualisation propre dans le terminal

INIT()
def Banner():
    tool_name  = "WebScanner-X"
    version    = "1.00"
    start_time = datetime.now().strftime("%Y-%m-%d _ %H:%M:%S")

    print("\n")
    print(f"|{VERT}-------------------------------------{RESET}|")
    print(f"|{LUMINEUX}Start{RESET}     : {BLEU}{start_time}{RESET}    |")
    print(f"|{LUMINEUX}Programme{RESET} : {VERT}{tool_name}{RESET}             {RESET}|")
    print(f"|{LUMINEUX}Version{RESET}   : {version}                     |")
    print(f"|{ROUGE}-------------------------------------{RESET}|")
    print(f"|{ROUGE}Dev{RESET}       : {JAUNE}@Cyber-Tchak{RESET}             |")
    print(f"|{ROUGE}GitHub{RESET}    : {JAUNE}inza57765-sketch{RESET}         |")
    print(f"|{VERT}-------------------------------------{RESET}|")
    print("\n\n")
