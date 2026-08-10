from datetime import datetime
"""
ce fichier gerèr le bannere de l'outil
"""
# cette fonction donne une visualisation propre dans le terminal
def Banner():
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
