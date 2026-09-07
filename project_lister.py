import subprocess as sub

def project_tree():
    try:

        tree = sub.run(["tree"], capture_output=True, text=True)
        print("\nWebScanner-X : Tree")
        print(tree.stdout)
        print("---"*16)

    except FileNotFoundError:
        print("\nWebScanner-X : paquet tree non installer")

