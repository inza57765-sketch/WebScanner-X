"""
Affichage
Response 404 :
"""
def not_found(result):

    print("\n\tla page est inaccessible....\n")

    print(result["url"])
    print("______________________________________")
    print(f"Status : {result['status_code']}")
    print("______________________________________")

    print("\n")
