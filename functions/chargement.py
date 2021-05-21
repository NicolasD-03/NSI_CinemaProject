def chargement(nom):

    """Charge chaque ligne du fichier dans une liste de tuple

    Args:
        :params nom(string): Nom du fichier

    Returns:
        :return table(list): Liste de tuples correspondant au contenu du fichier
    """

    #Initialisation de la liste de tuple
    table = []

    #Ouverture du fichier en écriture seulement
    fichier = open("data/dataBase/"+nom+".csv", 'r', encoding="UTF-8")

    #Skip de la première ligne
    lignes = fichier.readlines()[1:]

    #Boucle pour chaque ligne du fichier
    for ligne in lignes:
        #Séparation de chaque ligne et suppression du "\n"
        list_ligne = ligne[:-1].split(";")
        #Ajout dans la liste "table" chaque ligne au format de tuple
        table.append(tuple(list_ligne))
    
    #Fermeture du fichier
    fichier.close()

    return table
    

if __name__ == "__main__":

    tab = chargement("acteurs")

    for i in range (0, 10):
        print(tab[i])
    