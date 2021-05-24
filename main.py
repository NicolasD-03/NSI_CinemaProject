from functions.chargement import *
from functions.recherche import *

if __name__ == "__main__":
    
    #Initialisation des tabs
    films_tab = chargement("films")
    acteurs_tab = chargement("acteurs")
    realisateurs_tab = chargement("realisateurs")

    #Toutes les fonctions

    #Affichage fonction sur 1 table
    print("\n---------- Fonctions sur 1 table ----------")
    films_commencant_par(films_tab, "L")
    langues(films_tab)
    acteurs_prenoms(acteurs_tab, "Bruce")
    films_sortis_avant(films_tab, 1931)
    films_genre(films_tab, "Action")
    print("\n-------------------------------------------")

    # # #Affichage fonction d'agrégation
    print("\n---------- Fonctions d'agrégation ----------")
    print(nb_acteurs(acteurs_tab))
    print(nb_films_langues(films_tab, "cn"))
    print(nb_films_titre(films_tab, "Batman"))
    print(nb_films_argent(films_tab, 10000000))
    print("\n--------------------------------------------")

    # #Affichage fonction sur 2 tables
    print("\n---------- Fonctions sur 2 tables ----------")
    films_choix(acteurs_tab, films_tab, "Bruce Willis")
    films_choix(realisateurs_tab, films_tab, "Luc Besson")
    acteur_categorie(acteurs_tab, films_tab, "Cameron Diaz", "Comedy")
    print("\n--------------------------------------------")

    # # #Affichage fonctions sur 3 tables
    print("\n---------- Fonctions sur 3 tables ----------")
    acteur_film_long(films_tab, realisateurs_tab, acteurs_tab, "Martin Scorsese")
    real_est_acteur(films_tab, realisateurs_tab, acteurs_tab)
    print("\n--------------------------------------------")

    # #Création du fichier bdd_cinema.csv
    print("\n---------- Création du fichier bdd_cinema.csv ----------")
    assemble(films_tab, realisateurs_tab, acteurs_tab)
    print("\n--------------------------------------------------------")
    