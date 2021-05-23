#!!!!! Enlever des commentaire si ce fichier est executé !!!!!
# from affichage import *
# from chargement import * 

#!!!!! Mettre en commentaire si ce fichier est executé !!!!!
from functions.affichage import *

def films_commencant_par(tab, lettre):

    """Affiche tout les films dont le nom commence par "lettre"

    Args:
        :params tab(list): Liste où executer la recherche
        :params lettre(char): Première lettre du film 
    """
    #Ajoute à "table_titre" chaque nom de film ayant pour première character "lettre"
    table_titre = [tab[i][1] for i in range(0, len(tab)) if tab[i][1][0].lower() == lettre.lower()]

    #Si le nombre de film est entre 0 et 10 on les affiche tous
    if len(table_titre) > 0 and len(table_titre) < 10:
        #Affichage du nombre de film ainsi que la 1ère lettre
        print("\nVoici les", (len(table_titre)), "films commencent par \"" + lettre + "\"")
        #Affichage des films
        affiche_table(table_titre, 1, len(table_titre))

    #Si le nombre de film on affiche seulement 10 films
    elif len(table_titre) >= 10:
        #Affichage du nombre de film ainsi que la 1ère lettre
        print("\nVoici les 10 premiers films commencent par \"" + lettre + "\"")
        #Affichage des films
        affiche_table(table_titre, 1, 10)

    #Affichage du nombre total de film
    print("Nombre total de film : ", len(table_titre))

def langues(tab):

    """Affiche tout les sigles de toutes les langues des films

    Args:
        :params tab(list): Liste où executer la recherche
    """
    #Initialisation de la liste des langues
    lang_sigle = []

    #Boucle pour chaque film
    for i in range(0, len(tab)):
        #Récupère la langue du film
        lang_film = tab[i][4]
        #Si elle n'est pas déjà dans la liste des langues
        if lang_film not in lang_sigle:
            #Ajout de la langue du film dans la liste des langues
            lang_sigle.append(lang_film)

    #Trie par ordre alphabétique
    lang_sigle.sort()

    #Affichage du nombre d'acteurs et du prénom
    print("\n Voici les 10 premieres langues")

    #Affichage des 10 premiers acteurs
    affiche_table(lang_sigle, 1, 10)

    #Affichage du nombre total de langue
    print("Nombre total de langue", len(lang_sigle))

def acteurs_prenoms(tab, prenom):

    """Affiche tous les acteurs avec le prénom que l'on veut

    Args:
        :params tab(list): Liste où executer la recherche
        :params prenom(string): Nom de l'acteur
    """

    #Initialisation de la liste des acteurs unique
    acteur_list = []

    #Boucle pour chaque ligne de "tab"
    for i in range (0, len(tab)):
        #Récupère le prénom de l'acteur
        acteur_prenom = tab[i][1]
        #Si il n'est pas dans "acteur_list" alors
        if acteur_prenom not in acteur_list:
            #Ajout du nom de l'acteur dans "acteur_list"
            acteur_list.append(acteur_prenom)

    #Ajoute à "acteur_prenom" chaque prenom d'acteur commencant par "prenom"
    acteur_prenom = [acteur_list[i] for i in range(0, len(acteur_list)) if acteur_list[i].split()[0] == prenom]

    #Si le nombre d'acteurs dans "acteur_prenom" est > 0 et < 10 alors on les affiche tous
    if len(acteur_prenom) > 0 and len(acteur_prenom) < 10:
        #Affichage du nombre d'acteurs et du prénom
        print("\nVoici les", len(acteur_prenom), "acteurs commencent par", "\"" + prenom + "\"")
        #Affichage des acteurs
        affiche_table(acteur_prenom, 1, len(acteur_prenom))
    #Si le nombre d'acteurs dans "acteur_prenom" est  > 10 alors on en affiche que 10
    elif len(acteur_prenom) >= 10:
        #Affichage du nombre d'acteurs et du prénom
        print("\nVoici les 10 premiers acteurs commencent par", "\"" + prenom + "\"")
        #Affichage des 10 premiers acteurs
        affiche_table(acteur_prenom, 1, 10)

    #Affichage du nombre d'acteurs total
    print("Acteurs total :", len(acteur_prenom))

def films_sortis_avant(tab, annee):

    """Affiche tous les films sortis avant "annee"

    Args:
        :params tab(list): Liste où executer la recherche
        :params annee(int): Année de sortie du film
    """

     #Ajoute à "list_film" chaque nom de film qui sont sortie avant "annee"
    list_film = [tab[i][1] for i in range(0, len(tab)) if int(tab[i][2]) < annee]
    
    #Si le nombre de film dans "list_film" est > 0 et < 10 alors on les affiche tous
    if len(list_film) > 0 and len(list_film) < 10:
        #Affichage du nombre de film et l'année de sortie 
        print("\nVoici les", len(list_film),"films sortie avant", annee)
        #Affichage des films
        affiche_table(list_film, 1, len(list_film))
    #Si le nombre de film dans "list_film" est > 10 alors on affiche les 10 premiers 
    elif len(list_film) >= 10:
        #Affichage du nombre de film et l'année de sortie
        print("\nVoici les 10 premiers films sorties avant", annee)
        #Affichage des films
        affiche_table(list_film, 1, 10)

    #Affichage du nombre total de film sortie avant "annee"
    print("Nombre total de film sortie avant", annee, ":", len(list_film))    

def films_genre(tab, genre):

    """Affiche tous les Id des film ayant pour genre "genre"

    Args:
        :params tab(list): Liste où executer la recherche
        :params genre(string): Genre du film
    """

    #Ajoute à "list_film" chaque ID de film ayant pour genre "genre"
    list_film = [tab[i][0] for i in range(0, len(tab)) if genre in tab[i][5].split(",")]
    
    #Si le nombre de film dans "list_film" est > 0 et < 10 alors on les affiche tous
    if len(list_film) > 0 and len(list_film) < 10:
        #Affichage du nombre de film et l'année de sortie 
        print("\nVoici l'ID des", len(list_film),"films ayant pour genre", "\"" + genre + "\"")
        #Affichage des films
        affiche_table(list_film, 1, len(list_film))
    #Si le nombre de film dans "list_film" est > 10 alors on affiche les 10 premiers 
    elif len(list_film) >= 10:
        #Affichage du nombre de film et l'année de sortie
        print("\nVoici l'ID des 10 premiers films ayant pour genre", "\"" + genre + "\"")
        #Affichage des films
        affiche_table(list_film, 1, 10)

    #Affichage du nombre total de film sortie avant "annee"
    print("Nombre total de film ayant pour genre", "\"" + genre + "\"", ":", len(list_film))  

def nb_acteurs(tab):

    """Retourne le nombre d'acteurs différents

    Args:
        :params tabs(list): Liste où executer la recherche

    Returns:
        :return (int): Le nombre d'acteurs
    """
    #Initialisation de la liste d'acteur unique
    acteur_list = []

    #Boucle pour chaque ligne dans "tab"
    for i in range(0, len(tab)):
        #Recupère le nom de l'acteur
        acteur_name = tab[i][1]
        #Vérification si le nom de l'acteur n'est pas dans "acteur_list"
        if acteur_name not in acteur_list:
            #Si il n'y est pas on l'ajoute
            acteur_list.append(acteur_name)

    return len(acteur_list) 

def nb_films_langues(tab, langue):

    """Renvoie le nombre de film dans la langue "langue"

    Args:
        :params tab(list): Liste où executer la recherche
        :params langue(string): Langue du film

    Returns:
        :return (int): Nombre de film d'une langue
    """
    #Ajoute à "film_list" chaque film ayant pour langue "langue"
    film_list = [tab[i][4] for i in range(0, len(tab)) if tab[i][4] == langue]

    return len(film_list)

def nb_films_titre(tab, chaine):

    """Renvoie le nombre de films contenant le mot "chaine"

    Args:
        :params tab(list): Liste où executer la recherche
        :params chaine(string): Mot dans le titre du film

    Returns:
        :return (int): Nombre de films ayant "chaine" dans le titre
    """

    #Ajoute à "film_list" chaque film ayant dans leur titre "chaine"
    film_list = [tab[i][0] for i in range(0, len(tab)) if chaine in tab[i][1].split()]

    return len(film_list)

def nb_films_argent(tab, somme):

    """Renvoie le nombre de films ayant rapporté plus que la somme "somme"

    Args:
        :params tab(list): Liste où executer la recherche
        :params somme(int): Somme d'argent minimal

    Returns
        :return (int): Nombre de film ayant rapporté plus que "somme"
    """

    #Ajoute à "film_list" chaque film ayant rapporté plus que "somme"
    film_list = [tab[i][0] for i in range(0, len(tab)) if int(tab[i][6]) > somme]

    return len(film_list)

def films_choix(tab1, tab2, nom):

    """Affiche tous les titres des films de l'acteur ou du réalisateur "nom"

    Args:
        :params tab1(list): Liste1 où executer la recherche
        :params tab2(list): Liste film où executer la recherche
        :params nom(string): Nom de l'acteur ou du réalisateur
    """
    #Initalisation de la liste de film
    list_film = []

    #Ajoute à "id_film" chaque ID de film ayant pour réalisateur/acteur "nom"
    id_film = [tab1[i][0] for i in range(0, len(tab1)) if tab1[i][1] == nom]

    #Boucle pour chaque film
    for i in range(0, len(tab2)):
        #Condition si l'ID du film est dans "id_film"
        if tab2[i][0] in id_film:
            #Si vrai alors on ajoute le nom du film dans "list_film"
            list_film.append(tab2[i][1])

    #Si le nombre de film dans "list_film" est > 0 et < 10 alors on les affiche tous
    if len(list_film) > 0 and len(list_film) < 10:
        #Affichage du nombre de film et l'année de sortie 
        print("\nVoici les", len(list_film),"films ou", nom, "est acteur/actrice ou réalisateur/réalisatrice")
        #Affichage des films
        affiche_table(list_film, 1, len(list_film))
    #Si le nombre de film dans "list_film" est > 10 alors on affiche les 10 premiers 
    elif len(list_film) >= 10:
        #Affichage du nombre de film et l'année de sortie
        print("\nVoici les 10 premiers films ou", nom, "est acteur/actrice ou réalisateur/réalisatrice")
        #Affichage des films
        affiche_table(list_film, 1, 10)

    #Affichage du nombre total de résultat
    print("Nombre total de résultat de film ou", nom, "est acteur/actrice ou réalisateur/réalisatrice:", len(list_film))

def acteur_categorie(tab1, tab2, nom, genre):
    """Affiche touts les titres des films qui ont pour acteurs "nom" et comme genre "genre"

    Args:
        :param tab1(list): Liste des acteurs où executer la recherche
        :pram tab2(list): Liste des film où executer la recherche
        :param nom(string): Nom de l'acteur
        :param genre(string): Genre du film*
    """

    #Initalisation de la liste de film
    list_film = []

    #Ajoute à "id_film" chaque ID de film ayant pour réalisateur/acteur "nom"
    id_film = [tab1[i][0] for i in range(0, len(tab1)) if tab1[i][1] == nom]

    #Boucle pour chaque film
    for i in range(0, len(tab2)):
        #Condition si l'ID du film est dans "id_film" et que "genre" soit dans le genre du film
        if tab2[i][0] in id_film and genre in tab2[i][5].split(","):
            #Si vrai alors on ajoute le nom du film dans "list_film"
            list_film.append(tab2[i][1])
    
    #Si le nombre de film dans "list_film" est > 0 et < 10 alors on les affiche tous
    if len(list_film) > 0 and len(list_film) < 10:
        #Affichage du nombre de film et l'année de sortie 
        print("\nVoici les", len(list_film),"films ou", nom, "est acteur/actrice et que le genre est", "\"" + genre + "\"")
        #Affichage des films
        affiche_table(list_film, 1, len(list_film))
    #Si le nombre de film dans "list_film" est > 10 alors on affiche les 10 premiers 
    elif len(list_film) >= 10:
        #Affichage du nombre de film et l'année de sortie
        print("\nVoici les 10 premiers films ou", nom, "est acteur/actrice et que le genre est", "\"" + genre + "\"")
        #Affichage des films
        affiche_table(list_film, 1, 10)
    #Affichage du nombre total de résultat
    print("Nombre total de résultat de film ou", nom, "est acteur/actrice et que le genre est", "\"" + genre + "\" :", len(list_film))
    
def acteur_film_long(tab1, tab2, tab3, nom):
    """Affiche les acteurs du film le plus long réalisé par "nom"

    Args:
        :params tab1(list): Liste des films où executer la recherche
        :params tab2(list): Liste des réalisateurs où executer la recherche
        :params tab3(list): Liste des acteurs où executer la recherche
        :params nom(string): Nom du réalisateur
    """

    #Initialisation du dictionnaires de l'ID et de la durée du film le + long
    film_long = {
        "id": 0,
        "duree": 0
    }

    #Ajoute à "film_real" chaque ID des films où le réalisateur est "nom"
    film_real = [tab2[i][0] for i in range(0, len(tab2)) if nom ==tab2[i][1]]

    #Boucle pour chaque film
    for i in range(0, len(tab1)):
        #Vérification si l'ID du film est dans "film_real"
        if tab1[i][0] in film_real:
            #Si oui
            #Vérification si la durée du film est plus long que celle de "film_long[duree]"
            if int(tab1[i][3]) > film_long["duree"]:
                #Si oui on met à jour "film_long" avec l'id et la duree du film le plus long
                film_long["id"] = int(tab1[i][0])
                film_long["duree"] = int(tab1[i][3])
    
    #Ajoute à "acteur_list" chaque nom d'acteur si "film_long["id"]" est égal à l'ID du film où l'acteur à joué
    acteur_list = [tab3[i][1] for i in range(0, len(tab3)) if film_long["id"] == int(tab3[i][0])]

    #Si le nombre d'acteur dans "acteur_list" est > 0 et < 10 alors on les affiche tous
    if len(acteur_list) > 0 and len(acteur_list) < 10:
        #Affichage du nombre d'acteur et du nom du réalisateur
        print("\nVoici les", len(acteur_list),"acteurs ayant joués dans le films le plus long de", nom)
        #Affichage des acteurs
        affiche_table(acteur_list, 1, len(acteur_list))
    #Si le  nombre d'acteur dans "acteur_list" est > 10 alors on affiche les 10 premiers 
    elif len(acteur_list) >= 10:
        #Affichage du nombre d'acteur et du nom du réalisateur
        print("\nVoici les 10 premiers acteurs ayant joués dans le films le plus long de", nom)
        #Affichage des acteurs
        affiche_table(acteur_list, 1, 10)
    #Affichage du nombre total de résultat
    print("Nombre total d'acteurs ayant joués dans le film le plus long de", nom, ":" ,len(acteur_list))

def real_est_acteur(tab1, tab2, tab3):
    """Affiche les films où l'acteur est aussi réalisateur

    Args:
        :params tab1(list): Liste des films où executer la recherche
        :params tab2(list): Liste des réalisateurs où executer la recherche
        :params tab3(list): Liste des acteurs où executer la recherche
    """
    #Initialisation de la liste des acteurs
    list_acteurs = []

    #Initialisation de la liste de id des films réalisé par le réalisateur
    id_film_real = []
    #Initialisation de la liste des id des films joué par le réalisateurs
    id_film_act = []

    #Initialisation de la liste des id où le réalisateurs est acteur et réalisateur 
    id_film_act_real = []

    #Boucle pour chaque acteurs
    for i in range(0, len(tab3)):
        #On ajoute le nom de chaque acteur à "list_acteurs"
        list_acteurs.append(tab3[i][1])

    #Boucle pour chaque réalisateur
    for index_real in range(0, len(tab2)):
        #Vérification si le nom du réalisateur est dans "list_acteurs"
        if tab2[index_real][1] in list_acteurs:
            #Si oui
            #Boucle pour chaque acteurs
            for film_acteur in range(0, len(tab3)):
                #Vérification si le nom de l'acteurs est = au nom du réalisateur
                if tab3[film_acteur][1] == tab2[index_real][1]:
                    #Si oui
                    #On ajoute l'id du film où le réalisateur est acteur à "id_film_act"
                    id_film_act.append(tab3[film_acteur][0])

            #On ajoute l'id du film qui a été réalisé par le réalisateur
            id_film_real.append(tab2[index_real][0])

        #Boucle pour chaque films
        for index_film_real in range(0, len(id_film_real)):
            #vérification si l'id du film réalisé par le réalisateur et dans l'id du film où le réalisateur est acteur
            if id_film_real[index_film_real] in id_film_act:
                #Si oui
                #On ajoute l'id du film à la liste des films où l'acteur est réalisateur et acteur
                id_film_act_real.append(id_film_real[index_film_real])
        #On vide les id des films où le réalisateur est acteur
        id_film_act.clear()
        #On vide les id des films réalisé par le réalisateur
        id_film_real.clear()

    #Ajoute à "nom_film_act_real" chaque nom des films quand l'id du film est dans la liste des films où l'acteur est réalisateur
    nom_film_act_real = [tab1[i][1] for i in range(0, len(tab1)) if tab1[i][0] in id_film_act_real]
    
    #Si le nombre d'acteur dans "nom_film_act_real" est > 0 et < 10 alors on les affiche tous
    if len(nom_film_act_real) > 0 and len(nom_film_act_real) < 10:
        #Affichage du nombre d'acteur et du nom du réalisateur
        print("\nVoici les", len(nom_film_act_real),"films où le réalisateur et aussi acteur")
        #Affichage des acteurs
        affiche_table(nom_film_act_real, 1, len(nom_film_act_real))
    #Si le  nombre d'acteur dans "nom_film_act_real" est > 10 alors on affiche les 10 premiers 
    elif len(nom_film_act_real) >= 10:
        #Affichage du nombre d'acteur et du nom du réalisateur
        print("\nVoici les 10 premiers films où le réalisateur et aussi acteur")
        #Affichage des acteurs
        affiche_table(nom_film_act_real, 1, 10)
    #Affichage du nombre total de résultat
    print("Nombre total de films où le réalisateur et aussi acteur" ,len(nom_film_act_real))    

# if __name__ == "__main__":
    # films_tab = chargement("films")
    # acteurs_tab = chargement("acteurs")
    # realisateur_tab = chargement("realisateurs")
    # films_commencant_par(films_tab, "l")
    # langues(films_tab)
    # acteurs_prenoms(acteurs_tab, "Bruce")
    # films_sortis_avant(films_tab, 1935)
    # films_genre(films_tab, "Action")
    # print(nb_acteurs(acteurs_tab))
    # print(nb_films_langues(films_tab, "cn"))
    # print(nb_films_titre(films_tab, "Batman"))
    # print(nb_films_argent(films_tab, 10000000))
    # films_choix(acteurs_tab, films_tab, "Bruce Willis")
    # acteur_categorie(acteurs_tab, films_tab, "Cameron Diaz", "Comedy")
    # acteur_film_long(films_tab, realisateur_tab, acteurs_tab, "Martin Scorsese")
    # real_est_acteur(films_tab, realisateur_tab, acteurs_tab)