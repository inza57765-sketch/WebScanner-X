#!/usr/bin/env python3

import argparse
from . import (
     Version,
     outil_aide,
     Source_Code,
     cli_readme,
     project_tree
)
from .core.modules.dns_lookup  import dns_trad



def WebScanner_run():
    try:
        class WebScannerParser(argparse.ArgumentParser):

            def error(self, message):
                print("\n")
                print(f"[WebScanner-X] : {message}")
                print('Utilisez "WebScan --help" pour obtenir de l’aide.')
                self.exit(2)




        parser = WebScannerParser(
            prog="WebScanner-X",
            add_help=False,
            description="Un outil CLI permettant d'analyser les informations HTTP d'un serveur Web."
        )





        parser.add_argument(
            "-h","--help", "--helps",
            help="Afficher une aide Personnalisé.",
            action="store_true"
        )
        group = parser.add_mutually_exclusive_group(required=False)



        group.add_argument(
            "--scan",
            metavar="URL",
            help="Scanner une URL."
        )

        group.add_argument(
            "--dns",
            metavar="DOMAINE",
            help="Résoudre un domaine en une adresse ip."
        )

        group.add_argument(
            "--version",
            action="store_true",
            help="Afficher la version."
        )

        group.add_argument(
            "--readme",
            action="store_true",
            help="Afficher le readme."
        )

        group.add_argument(
            "--tree",
            action="store_true",
            help="Aficher l'arborescence."
        )
        args = parser.parse_args()




        if args.scan:
            base_url = args.scan
            Source_Code(base_url)



        elif args.dns:
            dns_trad(args.dns)




        elif args.help:
            outil_aide()

        elif args.version:
            Version()

        elif args.readme:
            cli_readme()

        elif args.tree:
            project_tree()


        else:
            parser.print_help()


    except KeyboardInterrupt:
        print("\nWebScanner-X : Interruption Clavier.")

    except Exception as erreur:
        print(f"\nWebScanner-X : {erreur}.")
