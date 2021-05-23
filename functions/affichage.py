#!!!!! Enlever des commentaire si ce fichier est executé !!!!!
#from chargement import *

def affiche_table(tab, deb, fin):

    """Affiche une liste de "tab" en partant de l'index "deb" jusqu'à l'index "fin"

    Args:
        :params tab(list): Liste à afficher
        :params deb(int): Index de début
        :params fin(int): Index de fin
    """
    #Initialisation de la liste à afficher
    list_afficher = []
    #Initialistation de la longueur de l'élément de la liste le plus long 
    max_len = -1

    #Boucle pour chaque ligne compris entre l'index de début et de fin dans la liste demandée
    for ligne in range(deb, fin+1): 
        #Ajout de chaque ligne dans la liste "list_afficher"
        list_afficher.append(tab[ligne-1])

    #Boucle pour chaque element dans la liste "list-afficher"
    for element in list_afficher:
        #Vérification si la longueur de "element" est > à "len_max"
        if len(element) > max_len:
            #Si c'est vrai modification de "len_max" par la longueur de "element"
            max_len = len(element)


    #----- Affichage -----#

    #Affichage de la décoration supérieure
    print("+" + "-"*(max_len+2) + "+" )

    #Boucle pour chaque element dans la liste "list_afficher"
    for element in list_afficher:
        #Affichage de l'element avec les décorations au début et à la fin
        print("| " + element + " "*(max_len-len(element)+1) + "|")

    #Affichage de la décoration inférieur
    print("+" + "-"*(max_len+2) + "+" )

if __name__ == "__main__":
    tab_dist = chargement("acteurs")
    tab_exe = [tab_dist[i][1] for i in range(0, len(tab_dist))]
    affiche_table(tab_exe, 10, 20)