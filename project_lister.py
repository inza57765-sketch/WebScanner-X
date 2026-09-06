import subprocess as sub

def project_tree():
    tree = sub.run(["tree"], capture_output=True, text=True)
    print("\n")
    print("WebScanner-X : Tree")
    print("-"*59)

    print(tree.stdout)
    print("-"*59)
