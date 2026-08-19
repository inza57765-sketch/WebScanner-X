"""
ce fichier est l'animateur des couleurs dans le terminal
"""


# cette fonction permet de chargé les couleurs nécessaires pour l'animation
from colorama import init, Fore, Back, Style

INIT = init
RESET    = "\033[00m"
VERT    = Fore.GREEN
BLEU     = Fore.BLUE
JAUNE    = Fore.YELLOW
ROUGE    = Fore.RED
LUMINEUX = Style.BRIGHT