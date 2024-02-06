""" 
Script permettant à :
- comparer les éléments d'un fichier 1 avec ceux d'un fichier 2
- signaler la présence d'éléments identiques
- signaler la présence d'élements similaires
- signaler la présence d'éléments où une faute de frappe est possible
"""
def lecture_fichier(lien):
    with open(lien,'r') as f:
        txt = f.readlines()
        contenu_fichier = [c.strip() for c in txt]
    return contenu_fichier


def verification(fichier1,fichier2):
    global liste_des_elements_manquant
    global liste_des_elements_present
    global liste_des_fautes_possibles
    elements_fichier1 = lecture_fichier(fichier1)
    elements_fichier2 = lecture_fichier(fichier2)


    liste_des_elements_manquant = []
    liste_des_elements_present = []
    liste_des_fautes_possibles = []

    for i in elements_fichier2:#selectionne les éléments du fichier 2, 1 par 1 pour les faire passer dans la boucle
        nb_lettres_idd = 0#pour reset à chaque ligne le nombre de lettres identiques (voir apres)
        if i in elements_fichier1:#vérifie si l'élément selectionné est présent dans le fichier 1            
            liste_des_elements_present.append(i)
            elements_fichier1.remove(i)
            continue
        elif i not in elements_fichier1:#si élément non présent suite           
            for element in elements_fichier1:#cherche dans les éléments fichier 1
                nb_lettres_idd = 0
                if abs(len(element)-len(i)<= 2) and element not in elements_fichier2:#si 1 élément à le même nombre de lettre + ou - 1 et n'est pas présent dans les éléments du fichier 2
                    for lettre in element:#recupere les lettres de cet élément                                                                                               
                        if lettre in i:#si une lettre est présente dans un des éléments du fichier 2 suite                            
                            nb_lettres_idd += 1#ajoute 1 au nombre de lettre identiques
                    if nb_lettres_idd >= len(i) - 3:#compare si le nombre de lettre idd est suffisant pour dire que c'est une erreur (3 actuellement)                            
                        liste_des_fautes_possibles.append(element)                                             
                        continue
                        
                    else:#s'il ne sagit pas d'une erreur
                        continue#passe
                else:#si le nombre de lettre est différent à + que + ou - 1                    
                    liste_des_elements_manquant.append(i)
        else:
            break

fichier1 = input("Nom du fichier fichier 1 : ")
fichier2 = input("Nom du fichier fichier 2 : ")
verification(fichier1, fichier2)
if liste_des_elements_manquant == []:
    print("-"*50)
    print("")
    print("[OK] Logs complète")
    print("")
    print("-"*50)
else :
    print("-"*50)
    print("")
    print(f"Eléments manquants : {liste_des_elements_manquant}")
    print("")
    print("-"*50)
    print("")
    print(f"Eléments présents : {liste_des_elements_present}")
    print("")
    print("-"*50)
    print("")
    print(f"Fautes possibles : {liste_des_fautes_possibles}")
    print("")
    print("-"*50)


    


