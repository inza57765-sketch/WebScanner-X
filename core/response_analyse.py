"""
ce fichier est l'analysueur du code status
"""

from Terminal_Visualisation import affiches

# cette fonction analyse le code rendue par le serveur
def response_analyse_run(result):
    if result["response"] == 200:
        affiches(result)

    elif result["response"] == 301:
        print("\nLe site propose une redirection permanente !")

    elif result["response"] == 500:
        print(f"\nErreur serveur le à répondu avec le code : {result["response"]}")
    else:
        print("\nLe site est inaccéssible")