# Auteur : AVLAH Adama Eliya
# Date   : 29/09/2024


def fonc_bienvenu():
    """ renvoie une chaine composée de mots de bienvenu pour les joueurs

    Précondition : aucune
    """
    chaine  = "\t\t\t" + "-"*45 + "\n" + "\t\t\t"+"| BIENVENU AUX JEUX DE MORPION (Tic-Tac-Toe)|\n"+ "\t\t\t"+"-"*45
    return chaine


#-----------------------------------------------------------
def init_grille(n:int)->list[list[str]]:
    """ renvoie une liste de liste de ligne n et de colonne n

    Précondition : n >0
    Exemple(s) :
    $$$
    """
    res = []
    for i in range(n):
        liste = []
        for j in range(n):
            liste.append('')
        res.append(liste)
    return res
            
def constru_chaine_grille(liste:list[list[str]])->str:
     """ Transforme la liste de liste en chaine d'affichage sous forme de
        grille

     Précondition : n > 0
     Exemple(s) :
     $$$
     """
     n = 3
     car = ''
     for i in range(n):
         car = car + '-'*19 + '\n'
         for j in range(n):
             car = car + f"|  {liste[i][j]}  " 
         car = car + '|\n'
     car = car + '-'*19
     return car
#-------------------------------------------

def affiche_grille(liste:list[list[str]])->None:
    """ affiche liste sous forme de grille

    Précondition : auncune
    """
    print(constru_chaine_grille(liste))
#-------------------------------------------
    
def remplire_liste(liste:list[list[int]])->list[list[int]]:
    """ permet de remplir la liste de liste de 1 à 9

    Précondition : aucune
    """
    nb = 1
    for i in range(3):
        for j in range(3):
            liste[i][j] = str(nb)
            nb += 1
    return liste

#---------------------------------------------
def saisi_joueur(name:str,liste:list):
    """ demande le numero de case aux aux joueurs

    Précondition : aucune
    """
    num_case = input(f"{name} entrer le numero de votre case : ")
    while not(num_case.isdigit()) or not(check_num_case(int(num_case))) or num_deja_saisi(liste, num_case):
        num_case = input(f"{name} entrer le numero de votre case : ")
    return num_case
#------------------------------------------------
def gagne_hor(liste:list[list[int]])->bool:
    """ Renvoie True si une liste dans liste contient les même
        elements

    Précondition : liste non vide
    Exemple(s) :
    gagne_hor([['O','X','O'],['X','X','X'],['X','O','O']])
    True
    $$$ gagne_hor([['O','X','O'],['X','O','X'],['X','O','O']])
    False
    $$$ gagne_hor([['O','O','O'],['X','O','X'],['X','O','O']])
    True
    $$$ gagne_hor([['O','X','O'],['X','X','X'],['O','O','O']])
    True
    """
    cpt = 0
    x = 2
    liste1 = []
    while cpt < len(liste):
        i = 0
        while i < len(liste) - 1 and liste[cpt][i] == liste[cpt][i+1]:
            i += 1
        liste1.append(i)
        cpt += 1
    return x in liste1
#----------------------------------------------------------
def gagne_ver(liste:list[list[int]])->bool:
    """ renvoie True si le joueur gagne verticalement

    Précondition : liste non vide
    Exemple(s) :
    $$$ gagne_ver([['X','X','O'],['X','O','X'],['X','O','O']])
    True
    $$$ gagne_ver([['O','O','O'],['X','O','X'],['X','O','O']])
    True
    $$$ gagne_ver([['O','X','O'],['X','X','O'],['X','O','O']])
    True
    $$$ gagne_ver([['O','O','O'],['X','X','X'],['X','O','O']])
    False
    """
    cpt = 0
    x = 2
    liste1 = []
    while cpt < len(liste):
        i = 0
        while i < len(liste) - 1 and liste[i][cpt] == liste[i+1][cpt]:
            i += 1
        liste1.append(i)
        cpt += 1
    return x in liste1
#-------------------------------------------------------------
def gagne_dia1(liste:list[list[str]])->bool:
    """ renvoie True si un joueur gagne diagonalement 

    Précondition : liste non vide
    Exemple(s) :
    $$$ gagne_dia1([['O','X','X'],['X','X','O'],['X','O','X']])
    True
    $$$ gagne_dia1([['O','X','O'],['X','X','O'],['X','O','O']])
    False
    $$$ gagne_dia1([['X','O','X'],['X','X','O'],['X','O','O']])
    True
    """
    cpt = 0
    i = 2
    while cpt < len(liste)-1 and liste[i][cpt] == liste[i-1][cpt+1]:
        cpt += 1
        i -= 1
    return not(cpt < len(liste) -1)
#---------------------------------------------------------------

def gagne_dia2(liste:list[list[str]])->bool:
    """ renvoie True si un joueur gagne diagonalement

    Précondition : liste non vide
    Exemple(s) :
    $$$ gagne_dia2([['O','X','X'],['X','O','O'],['X','O','O']])
    True
    $$$ gagne_dia2([['X','O','X'],['X','X','O'],['X','O','X']])
    True
    $$$ gagne_dia2([['X','O','X'],['X','X','O'],['X','O','O']])
    False
    """
    cpt = 0
    i = 0
    while cpt < len(liste)-1 and liste[i][cpt] == liste[i+1][cpt+1]:
        cpt += 1
        i += 1
    return not(cpt < len(liste) -1)
 #----------------------------------------------------------------
def check_num_case(n:int):
    """ renvoie True si n correspond à un numéro de case

    Précondition : n >0
    Exemple(s) :
    $$$ check_num_case(5)
    True
    $$$ check_num_case(10)
    False
    $$$ check_num_case(1)
    True
    $$$ check_num_case(0)
    False
    """
    return n in [1,2,3,4,5,6,7,8,9]
#-----------------------------------------------------------------
def num_deja_saisi(liste:list,n:int)->bool:
    """ Renvoie True si le numero d'une case est déja saisi

    Précondition : aucune
    Exemple(s) :
    $$$
    """
    return n in liste
#-------------------------------------------------------------------
def saisi_name()->list:
    """ renvoie une liste composé des noms des joueurs

    Précondition : aucune
    """
    liste = []
    for i in range(1,3):
        name = input(f"Nom du joueur{i} : ")
        liste.append(name)
    return liste
#--------------------------------------------------------------------
def affiche_message(liste:list[str])->None:
    """ affiche un message aux joueurs

    Précondition : liste non vide
    """
    print("",liste[0],"votre symbole est 'X' et c'est à vous de commencer le jeux.\n",liste[1],"votre symbole est 'O'.")
#--------------------------------------------------------------------
def grille_rempli(liste:list[list[str]])->bool:
    """ verifie si ma liste est rempli des symbol du jeux

    Précondition : liste non vide
    Exemple(s) :
    $$$ grille_rempli([['O','X','X'],['X','O','O'],['X','O','O']])
    True
    $$$ grille_rempli([['O','X','X'],['X','2','O'],['X','O','O']])
    False
    """
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[i][j].isdigit():
                return False
    return True
 #---------------------------------------------------------------------

#------------------------------------------------------------------------

def saisi_in_grille(liste:list[list[str]],n:str,cara:str)->list[list[str]]:
    """ saisi au numero n de liste

    Précondition : liste non vide
    Exemple(s) :
    $$$ saisi_in_grille_j2([['1','2','3'],['4','5','6'],['7','8','9']], '1')
    [['O','2','3'],['4','5','6'],['7','8','9']]
    $$$ saisi_in_grille_j2([['1','2','3'],['4','5','6'],['7','8','9']], '5')
    [['1','2','3'],['4','O','6'],['7','8','9']]
    """
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[i][j] == n:
                liste[i][j] = cara
    return liste
#------------------------------------------------------------------------
def affiche_gagnant(name:str)->None:
    """ affiche un message aux joueurs

    Précondition : name non vide
    """
    print(name,"félicitation vous avez gagner le jeux.")



