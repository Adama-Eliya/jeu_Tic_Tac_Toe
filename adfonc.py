# Auteur : AVLAH Adama Eliya
# Date   : 29/09/2024

def fonc_bienvenu():
     chaine = """
                ---------------------------------------------
                | BIENVENU AUX JEUX DE MORPION (Tic-Tac-Toe)|
                ---------------------------------------------               
              """
     return chaine


#-----------------------------------------------
def papier(tab:list):
        print("-"*(len(tab[0]*4)+1))
        for ligne in tab:
            print("| ", end="")
            print(" | ".join(ligne),end="")
            print(" |")
            print("-"*(len(ligne*4)+1))
#-----------------------------------------------
def saisi_coordonnee():
      coord = input("Entrer les coordonnées de votre case.\nExemple: 0 1 (signifie 1ère ligne 2ème colonne): ")
      liste = coord.split()
      liste1 = list(map(int,liste))
      return liste1
#-----------------------------------------------
def name_joueur():
      name1 = input("Nom du joueur1 : ")
      name2 = input("Nom du joueur2 : ")
      print(f"{name1} votre symbole est 'X' et c'est à vous de commencer.")
      print(f"{name2} votre symbole est 'O'")
      return name1,name2

#------------------------------------------------
def gagner_hor(liste:list,l:int,c:int):
    x = 0
    y = 0
    while True :
        if liste[x][y] == liste[x][y+1] == liste[x][y+2]!= " ": 
            boole = True 
            break    
        elif x!= l-1 and y == c -3:
            x +=1
            y = 0
        elif x == l-1 and y == c-3:
            boole =  False
            break
        else:
            if y < c -3:
                    y+=1
    return boole
#----------------------------------------------------
def gagne_dia(liste:list,c:int):
     liste1 = liste[0][:c-2]
     liste2 = liste[1][1:c-1]
     liste3 = liste[2][-1:c-2:-1]
     for i,j,k in zip(liste1,liste2,liste3):
          if i == j == k != " ":
               boole = True
               break
          else:
               boole = False
     return boole
#------------------------------------------------
def gagne_ver(liste:list):
     liste1 = liste[0][::1]
     liste2 = liste[1][::1]
     liste3 = liste[2][::1]
     for i,j,k in zip(liste1,liste2,liste3):
          if i== j== k != " ":
               boole = True
               break
          else :
               boole = False
     return boole
#------------------------------------------------
