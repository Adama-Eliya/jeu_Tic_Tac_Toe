# Jeu de Tic-Tac-Toe (Python Console)

Un jeu classique de Tic-Tac-Toe développé en Python pour la console.  
Le jeu permet à deux joueurs de s’affronter, avec affichage du plateau et détection automatique des conditions de victoire.

---

## Fonctionnalités

- Plateau de 3x3 affiché en console
- Jeu pour deux joueurs (X et O)
- Détection automatique de la victoire horizontalement, verticalement et diagonalement
- Gestion des cases déjà jouées
- Match nul détecté automatiquement
- Interface simple et intuitive en console
- Code structuré en fonctions modulaires pour faciliter la lecture et la maintenance

---

## Organisation du code

- `tictactoe.py` : fichier principal contenant la boucle de jeu
- `adfonc.py` : module contenant toutes les fonctions utiles :
  - Initialisation et affichage du plateau (`init_grille`, `affiche_grille`)
  - Saisie des joueurs et validation des cases (`saisi_joueur`, `num_deja_saisi`)
  - Vérification des conditions de victoire (`gagne_hor`, `gagne_ver`, `gagne_dia1`, `gagne_dia2`)
  - Gestion du remplissage du plateau et mise à jour des cases (`remplire_liste`, `saisi_in_grille`)
  - Messages de bienvenue et de victoire (`fonc_bienvenu`, `affiche_message`, `affiche_gagnant`)

---

## Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/Adama-Eliya/jeu_Tic_Tac_Toe.git
