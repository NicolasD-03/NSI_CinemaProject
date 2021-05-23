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
    
def assemble(tab1, tab2, tab3):
    """Créée un fichier bdd_cinema.csv qui contient les infos des films Id des films, Titre des films, Réalisateur des films, Casting des films

    Args:
        :params tab1(list): Liste des films où executer la recherche
        :params tab2(list): Liste des réalisateurs où executer la recherche
        :params tab3(list): Liste des acteurs où executer la recherche
    """

    #Initialisation du répertoire où enregistrer le fichier
    dest_path = "data/dataBase/"
    #Initialisation du champ de texte du casting
    casting = ""

    #Ouverture du fichier en écriture
    files = open(dest_path+"bdd_cinema.csv", "w", encoding="UTF-8" )

    #Ecriture de la 1ère ligne du fichier
    files.write("Cle;Titre_Original;Realisateur;Casting\n")

    #Boucle pour chaque film
    for film in range(0, len(tab1)):
        #Initialisation de l'ID du film +1
        id_film = film+1
        #Initialisation du nom du film
        titre = tab1[film][1]

        #Boucle pour chaque réalisateur
        for real in range(0, len(tab2)):
            #Vérification si l'ID du film est égal à l'ID d'un film dans la liste des réalisateur
            if tab1[film][0] == tab2[real][0]:
                #Si oui
                #Initialisation du nom du réalisateur correspondant au film
                nom_real = tab2[real][1]

        #Boucle pour chaque acteur
        for acteur in range(0, len(tab3)):
            #Vérification si l'ID du film est égal à l'ID d'un film dans la liste des acteurs
            if tab1[film][0] == tab3[acteur][0]:
                #Si oui
                #On ajoute à casting chaque acteurs qu'on trouve avec une "," à la fin
                casting = casting+tab3[acteur][1]+','
        #Initialisation du text final avec l'ID, le titre, le nom du real, les noms des acteurs pour le film
        text = str(id_film)+";"+str(titre)+";"+str(nom_real)+";"+str(casting[:-1])+"\n" #[:-1] pour supprimer la "," en trop à la fin des acteurs
        #Ecriture de la variable text dans le fichier
        files.write(text)
        #On video chaque variable
        text = ""
        titre = ""
        real = ""
        casting = ""

    #Fermeture du fichier
    files.close()

    print("\n Information: Fichier bdd_cinema.csv créé !")

if __name__ == "__main__":
    tab = chargement("acteurs")
    for i in range (0, 10):
        print(tab[i])
    films_tab = chargement("films")
    acteurs_tab = chargement("acteurs")
    realisateurs_tab = chargement("realisateurs")
    assemble(films_tab, realisateurs_tab, acteurs_tab)
    