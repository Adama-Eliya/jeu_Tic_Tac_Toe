# Auteur: AVLAH Adama Eliya
# Date  : 22/11/2024


####################
# Jeu du Tic Tac Toe
####################


if __name__ == '__main__':
    # éxécuté qd ce module n'est pas initialisé par un import.
    from adfonc import *
    
    print(fonc_bienvenu())
    name_joueur = saisi_name()
    affiche_message(name_joueur)
    liste = init_grille(3)
    grille = remplire_liste(liste)
    affiche_grille(grille)
    cpt = 0
    liste = []
    while cpt == 0:
        i = 0
        while i < 2 and not(gagne_hor(grille) or gagne_ver(grille) or gagne_dia1(grille) or gagne_dia2(grille) or grille_rempli(grille)):
            num = saisi_joueur(name_joueur[i],liste)
            liste.append(num)
            if i == 0:
                saisi_in_grille(grille,num,'X')
            else:
                saisi_in_grille(grille,num,'O')
            affiche_grille(grille)
            j= i
            i += 1

        if grille_rempli(grille):
            print("Vous avez fait un match null.")
            cpt = 1
        elif i < 2:
            cpt = 1
            affiche_gagnant(name_joueur[j])   
