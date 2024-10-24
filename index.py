# Auteur: AVLAH Adama Eliya
# Date  : 29/09/2024 

from adfonc import *   # importation de tous les fonctions du module adfonc

print(fonc_bienvenu())   

joueur = name_joueur()     # récupération des noms des joueurs
l = 3                       #  les dimension du tableau de jeu
c = 3       
grille = [[" " for i in range(c)] for i in range(l)]  # un tableau qui récupéres les symboles
papier(grille)
liste_coord = []
x = 0
diese = 30
while True :
      if x!= 0:
            print(f"C'est votre tour {joueur[0]} ")
      
      liste2 = saisi_coordonnee()  # récupération des coordonnées des cases du tableaux
      while True :
            if liste2[0]> l-1 or liste2[1]> c - 1:
                  print(f"{joueur[0]} les coordonnées saisis n'existent pas")  # vérifie si les coordonnées saisient existent !
                  liste2 = saisi_coordonnee()
            else:
                  break
            
      if tuple(liste2) in liste_coord:
            print("Coordonnée deja saisi !")  # vérifie si les coordonnées sont déja saisi !!
            continue
      else:
            liste_coord.append(tuple(liste2)) # ajout des coordonnées saisient à la liste des coordonnées déja saisient
      
      grille[liste2[0]][liste2[1]] = 'X'
      papier(grille)             # affichage du tableau de jeux
      if gagner_hor(grille,l,c) or gagne_dia(grille,c) or gagne_ver(grille):
            print(f"{joueur[0]} vous avez gagner le jeux")
            break
      else:                                                           # verifie le resultat du jeu
            if len(liste_coord) == 9:
                  print("Match Null")
                  break
            
            
      print("#"*diese)
      # partie du joueur 2
      print(f"C'est votre tour {joueur[1]}")
      liste3 = saisi_coordonnee()
      while True :
            if liste3[0]> l-1 or liste3[1]> c - 1:
                  print(f"{joueur[1]}les coordonnées saisis n'existent pas")
                  liste2 = saisi_coordonnee()
            else:
                  break
      if tuple(liste3) in liste_coord:
            print("Coordonnée deja saisi !")
            continue
      else:
            liste_coord.append(tuple(liste3))

      grille[liste3[0]][liste3[1]] = 'O'
      papier(grille)
      if gagner_hor(grille,l,c) or gagne_dia(grille,c) or gagne_ver(grille):
            print(f"{joueur[1]} vous avez gagner le jeux")
            break
      else:
            if len(liste_coord) == 9:
                  print("Match Null")
                  break      
      x = 1
      print("#"*diese)

           


