from functions.affichage import *

if __name__ == "__main__":
    table_dist = chargement("acteurs")
    table_show = [table_dist[i][1] for i in range (0, len(table_dist))]
    affiche_table(table_show, 1, 8)