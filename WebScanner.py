import sys
from core.code import Source_Code
#from core.HtmlCat import htmlcat_run

#Fichief'r d'orchestre
##########################################
def WeScanner_run():
    try:
       if len(sys.argv) == 3:
           print("Erreur :")


       base_url = sys.argv[1]
       Source_Code(base_url)

    except IndexError:
       print("\nUrl non définie")
    except KeyboardInterrupt:
       print("\nInteruption clavier")
##########################################


if __name__ == "__main__":
    WeScanner_run()
