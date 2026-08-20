from bs4 import BeautifulSoup as bs4


def pages_analyseur_func(result):
    h2_liste = []
    h3_liste = []
    inputs_liste = []
    images_liste = []

    html = result["response"].text
    soup = bs4(html,  "html.parser")
    titre = soup.find("h1")
    sous_titre = soup.find("h2")

    elements_h2 = soup.find_all("h2")
    elements_h3 = soup.find_all("h3")
    elements_input = soup.find_all("input")
    images_liste = []
    images = soup.find_all("img")
    
    
    if titre is not None:
        print(f"Titre : {titre}")
    if sous_titre is not None:
        print(f"Sous-titre : {sous_titre}\n")


    if elements_h2 is not None:
        for h2 in elements_h2:
            h2_liste.append(h2)
            #print(h2)

    if elements_h3 is not None:
        for h3 in elements_h3:
            h3_liste.append(h3)
            #print(h3)

    if elements_input is not None:
        for inputs in elements_input:
            inputs_liste.append(inputs)
            #print(input)

    if images is not None:
        for image in images:
            images_liste.append(image)
            #print(image)

    print(f"elements h2     : {len(h2_liste)}")
    print(f"elements h3     : {len(h3_liste)}")
    print(f"elements input  : {len(inputs_liste)}")
    print(f"elements img    : {len(images_liste)}")