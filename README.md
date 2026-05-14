# Tour de Hanoi – Modélisation en Python

**Période:** 2024

## 📋 Description du projet

Modélisation complète du jeu classique des **Tours de Hanoi** en Python, avec une interface graphique interactive utilisant **Python Turtle Graphics**. Ce projet démontre la maîtrise des algorithmes récursifs, de la gestion d'états et de l'interface utilisateur graphique.

### Objectif du jeu

Le jeu des Tours de Hanoi consiste à déplacer une pyramide de disques d'une tour à une autre en respectant une seule règle : **un disque plus grand ne peut jamais être placé sur un disque plus petit**.

### Fonctionnalités principales

- **Interface graphique interactive** : Affichage en temps réel des tours et des disques
- **Système de dialogue** : Saisie du nombre de disques et des mouvements souhaités
- **Validation des coups** : Vérification des règles du jeu
- **Système de score** : Suivi des performances et classement des joueurs
- **Annulation de coups** : Possibilité d'annuler le dernier mouvement
- **Visualisation de la solution** : Affichage automatique de la résolution optimale
- **Algorithme récursif** : Résolution automatique du puzzle

## 🖼️ Interface du jeu

L'application utilise **Python Turtle Graphics** pour une représentation visuelle intuitive :

<img width="948" height="822" alt="Hanoi1" src="https://github.com/user-attachments/assets/9b5e8c95-a04c-4e2a-a9da-556cea9cc2a1" />

<img width="825" height="390" alt="hanoi2" src="https://github.com/user-attachments/assets/97f173af-18a2-4356-ade0-841c92277082" />



## 🏗️ Architecture et fonctionnalités

### Partie A : Gestion du plateau de jeu

- **`init(n)`** - Initialise le plateau avec n disques
- **`nbDisques(plateau, numtour)`** - Compte les disques d'une tour
- **`disqueSup(plateau, numtour)`** - Retourne le disque supérieur d'une tour
- **`posDisque(plateau, numdisque)`** - Localise un disque sur le plateau
- **`verifDepl(plateau, nt1, nt2)`** - Valide les mouvements légaux
- **`verifVictoire(plateau, n)`** - Détermine si le joueur a gagné

### Partie B : Interface graphique avec Turtle

- **`dessinePlateau(n)`** - Dessine les trois tours et la base
- **`disque(nd, n, tour, haut, couleur)`** - Dessine un disque avec code couleur
- **`dessineDisque(nd, plateau, n)`** - Affiche un disque spécifique
- **`dessineConfig(plateau, n)`** - Affiche la configuration complète
- **`effaceDisque(nd, plateau, n)`** - Efface un disque
- **`effaceTout(plateau, n)`** - Réinitialise l'affichage

### Partie C : Interaction utilisateur

- **`lireCoords(plateau)`** - Récupère les entrées du joueur via dialogue
- **`jouerUncoup(plateau, n, x, y)`** - Exécute un coup et le visualise
- **`boucleJeu(plateau, n)`** - Boucle principale du jeu

### Partie D : Gestion de l'historique

- **`dernierCoup(coups)`** - Analyse le dernier mouvement
- **`annulerDernierCoup(coups)`** - Annule le dernier mouvement effectué

### Partie E : Système de score

- **`sauvScore(nom, n, ncoups)`** - Enregistre le score d'un joueur
- **`afficheScores(scores, n)`** - Affiche le classement des joueurs

### Partie F : Algorithme de résolution

- **`mouvement(n, i, j, k)`** - Algorithme récursif générant la solution optimale
- **`deplacement(liste, n)`** - Visualise la résolution étape par étape

## 🎮 Guide d'utilisation

### Lancer le jeu

```bash
python "PROJET FINAL.py"
```

### Étapes du jeu

1. **Sélectionner le nombre de disques** : Le dialogue demande le nombre de disques à déplacer (1-7 recommandé)
2. **Choisir la tour de départ** : Entrer le numéro (0, 1 ou 2) de la tour contenant les disques
3. **Choisir la tour d'arrivée** : Entrer la destination du disque supérieur
4. **Valider le coup** : Le programme affiche le mouvement et met à jour le plateau
5. **Annuler si nécessaire** : Possibilité d'annuler le dernier coup
6. **Gagner** : Placer tous les disques sur la tour 3 en ordre décroissant
7. **Voir la solution** : En cas de défaite, visualiser la résolution optimale

## 📊 Complexité et mathématiques

- **Nombre minimum de coups** : 2^n - 1 (où n = nombre de disques)
- **Exemples** :
  - 3 disques : 7 coups minimum
  - 4 disques : 15 coups minimum
  - 5 disques : 31 coups minimum
  - 10 disques : 1023 coups minimum

L'algorithme récursif `mouvement(n, i, j, k)` génère la séquence optimale de mouvements.

## 🎨 Système de couleurs

Les disques sont colorés pour améliorer la lisibilité :

- **Disque 1** : Jaune
- **Disque 2** : Bleu
- **Disque 3 et +** : Rouge

## 🛠️ Compétences développées

- **Programmation Python** : Structures de données, récursion, gestion de dictionnaires
- **Interface graphique** : Python Turtle Graphics, gestion d'événements
- **Algorithmique** : Récursion, optimisation, résolution de puzzles
- **Gestion d'état** : Historique de coups, sauvegarde de scores
- **Validation de données** : Vérification des règles du jeu
- **Expérience utilisateur** : Dialogues intuitifs, annulation de coups, affichage de solutions

## 📂 Composition du projet

| Langage | Pourcentage |
|---------|------------|
| Python | 100% |

## 📝 Notes importantes

- Le script utilise le module `turtle` pour la représentation graphique
- Le module `copy` est utilisé pour la copie profonde de structures (historique des coups)
- Le nombre maximum de coups autorisés = 2^n - 1 + 5n pour laisser une marge au joueur
- L'interface complète est basée sur les dialogues de Turtle pour la saisie utilisateur

---

**Auteur:** kikflash21  
**Type de projet:** Éducatif - Algorithmique et interfaces graphiques
