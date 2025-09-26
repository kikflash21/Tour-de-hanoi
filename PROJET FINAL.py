import turtle

import copy

turtle.speed(200)

#Debut de la partie A

def init(n) :
    tour_1 = []
    plateau = []
    for i in range(n, 0, -1) : #boucle permettant d'ajouter les disques dans l'ordre decroissant se terminant losque i = 1 (inclut)
        tour_1.append(i)
    plateau.append(tour_1)
    for i in range(2) :        #boucle permettant d'ajouter les tours 2 et 3 vides
        plateau.append([])
    return plateau

def nbDisques(plateau, numtour) :
    return len(plateau[numtour])

def disqueSup(plateau, numtour):
    if numtour < 0 or numtour > 2 or len(plateau[numtour]) == 0: #on verifie si la tour est vide ou si le numéro ne correspond pas, on renvoit -1 si ces conditions sont remplies
        return -1
    else: #si les conditions precedentes ne sont pas remplies, on renvoit -1 le disque superieur de cette tour
        tour = plateau[numtour]
        return tour[-1]
        
   

def posDisque(plateau, numdisque) :
    if len(plateau) == 3 : #on verifie que le plateau possede bien 3 tours
        for i in range(len(plateau)) : #boucle permettant de tester si le numero du disque est bien dans une tour, on suppose que le dique existe donc nous n'avons pas mis de else
            if numdisque in plateau[i] :
                return i
            

def verifDepl(plateau, nt1, nt2):
    if disqueSup(plateau, nt1) == -1 or disqueSup(plateau, nt2) !=-1 and disqueSup(plateau, nt1) > disqueSup(plateau, nt2): #on verifie les conditions qui, si elles sont remplies, rendent le deplacement impossible
        return False #on return donc False si elles sont remplies
    else:
        return True #et True si elles ne le sont pas
    



def verifVictoire(plateau, n) :
    if len(plateau) != 3: #on commence par verifier si le plateau possede le bon nombre de tours
        return False
    
    elif len(plateau[0]) != 0 or len(plateau[1]) != 0: #on regarde s'il ne reste pas des disques sur les tours 1 et 2, sinon on return False
        return False
    
    elif len(plateau) == 3 and nbDisques(plateau, 2) == n and disqueSup(plateau, 2) == 1 : #on verifie encore si le plateau possede le bon nombre de tours, puis si tous les disque sont bien sur la derniere tour et enfin si le disque superieur est bien le plus petit
        for x in range(0, n - 1) :  #boucle permettant de verifier si les disque dans la liste sont bien dans l'ordre decroissant (donc dans l'ordre croissant en partant du haut de la tour)
            if plateau[2][x] <= plateau[2][x + 1] or plateau[2][x] - plateau[2][x + 1] != 1:
                return False #s'ils ne sont pas dans l'ordre decroissant on return False
        return True #si toutes les conditions sont reunies on return True
    else :
        return False

#print(verifVictoire([[], [], [3, 4, 1]], 3))


#code principal permettant de verifier si l'utilisateur a gagne ou non, en lui demandant d'abord le nombre de disques
#n = int(input("Nombre de disques ?"))
#plateau = init(n)

#if verifVictoire(plateau, n) == True : 
    #print("C'est gagne")
#else :
    #print("C'est perdu")



# Debut de la partie B





def tour(n,x,y): # Fonction auxiliaire pour la question 1 qui permet de dessiner les tours selon ses coordonnees
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.fillcolor('gray') # Dessine les tours en gris
    turtle.begin_fill()
    turtle.forward(20 + n*20) # Longueur des tours qui dependront du nombres de disques (n)
    turtle.right(90)
    turtle.forward(6) # Largeur des tours
    turtle.right(90)
    turtle.forward(20 + n*20)
    turtle.left(180)
    turtle.end_fill()
    

def dessinePlateau(n): # Question 1
    turtle.up()
    turtle.goto(-300, -200) # Placement aux bonnes coordonnees
    turtle.down()
    turtle.fillcolor('gray')
    turtle.begin_fill()
    turtle.forward(110 + n*90) # Longueur de la barre qui dependra du nombres de disques (n)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(110 + n*90)
    turtle.right(90)
    turtle.forward(20)
    turtle.end_fill()
    d = 110 + n*90 - 18 # Calcul de la distance pour avoir les coordonnee d'apres le nombre de disque(n)
    x = d /3
    z = x / 2
    turtle.up()
    turtle.goto(-310+z, -217) # Se place aux bonnes coordonnees
    turtle.down()
    turtle.write("Tour 1") # Ajout de texte pour les tours 
    turtle.up()
    turtle.goto(-310+z+6+x, -217)
    turtle.down()
    turtle.write("Tour 2")
    turtle.up()
    turtle.goto(-310+z+6+x+6+x, -217)
    turtle.down()
    turtle.write("Tour 3")
    tour(n, -300+z, -200) # Coordonnees des tours calcule a partir des equations du dessus
    tour(n, -300+z+6+x, -200)
    tour(n, -300+z+6+x+6+x, -200)
    turtle.up()


    
def disque(nd, n, tour, haut, couleur): # fonctions auxilliaire pour la question 2
    d = 110 + n*90 - 18
    x = d /3
    z = x / 2
    turtle.up()
    turtle.goto(-300-(4 +nd*30)/2 +z+(6+x)*(tour-1), -220+(haut*20))
    turtle.down()
    turtle.fillcolor('white') #effacer les tracer precedents des tours
    turtle.begin_fill() # commence a effacer
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10 + nd*30) # Largeur du disque qui depend de nd
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10 + nd*30)
    turtle.right(90)
    turtle.end_fill()


def disque_effac(nd, n, tour, haut): # Fonction auxiliaire pour la question 3 qui redessine en blanc pour effacer les disques
    d = 110 + n*90 - 18
    x = d /3
    z = x / 2
    turtle.up()
    turtle.goto(-300-(4 +nd*30)/2 +z+(6+x)*(tour-1), -220+(haut*20))
    turtle.down()
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10 + nd*30)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(180)
    turtle.end_fill()
    turtle.pencolor('black')


def dessineDisque(nd, plateau, n): # Question 2
    for k in range(3):  # Parcours les tours afin de trouver le disque nd 
        if nd in plateau[k]:
            hyp = plateau[k]
            for i in range(len(hyp)): # Tri les disques pour pouvoir les dessiner avec une couleurs definie (se limite avec 3 disques, les disques superieur a 3 seront egalement de couleur rouge)
                if nd == hyp[i]:
                    if nd == 1:
                        couleur = "yellow"
                    elif nd == 2:
                        couleur = "blue"
                    else:
                        couleur = "red"
                    disque(nd, n, k+1, i+1, couleur) # Trace le disque nd apres avoir trouve sa position



def effaceDisque(nd, plateau, n): # Question 3
    d = 110 + n*90 - 18 # Reprend la meme equations du debut(question 1)
    x = d /3
    z = x / 2
    for k in range(3): # Explore les tours de la meme maniere que la question 2
        if nd in plateau[k]:
            hyp = plateau[k]
            for i in range(len(hyp)):
                if nd == hyp[i]:
                    disque_effac(nd, n, k+1, i+1)
                    tour(n, -300+z +(6+x)*k, -200)# On redessine les tours qui ont peut etre ete efface


def dessineConfig(plateau, n): # Question 4
    for i in range(1, n+1):  # Parcours tout les disques et les dessine avec la fonction dessineDisque
        dessineDisque(i, plateau, n)


def effaceTout(plateau, n): # Question 5
    for i in range(1, n+1): # Parcours tout les disques et les efface avec la fonction effaceDisque
        effaceDisque(i, plateau, n)


#print(dessinePlateau(3))
#print(dessineConfig([[3,2,1], [], []], 3))



# Debut de la partie C


def lireCoords(plateau): # Question 1
    ndepart = int(turtle.numinput("Tour de depart", "Numero de la tour de depart: ", minval = 0))
    while ndepart > 2 or ndepart < 0 or nbDisques(plateau, ndepart) == 0: # Filtre la tour de depart pour qu'elle ne soit pas vide et qu'elle soit entre 0 et 2
        if ndepart > 2 or ndepart < 0:
            print("Invalide, tour inexistante.") # Selon le cas on affiche si la tour est vide ou inexistante
        elif nbDisques(plateau, ndepart) == 0:
            print("Invalide, tour vide.")
        ndepart = int(turtle.numinput("Tour de depart", "Numero de la tour de depart: ", minval = 0))
    narriv = int(turtle.numinput("Tour d'arrivee", "Numero de la tour d'arrivee: ", minval = 0))
    while narriv > 2 or narriv < 0 or verifDepl(plateau, ndepart, narriv) == False: # Filtre la tour d'arrive pour qu'elle soit correcte et qu'elle ne compose pas un disque superieur a celle du depart
        if narriv > 2 or narriv < 0:
            print("Invalide, tour inexistante.")
        elif verifDepl(plateau, ndepart, narriv) == False: # Selon le cas, on affiche si la tour est inexistante ou incorrect
            print("Invalide, disque plus petit.")
        narriv = int(turtle.numinput("Tour d'arrivee", "Numero de la tour d'arrivee: ", minval = 0))
    return ndepart, narriv

#Question 2
def jouerUncoup(plateau, n, x = None, y = None): #les paramètres optionnels permettent d'annuler automatiquement un coup si le joueur le demande, sans avoir à taper les tours de depart et d'arrivee
    if x == None or y == None : 
        x, y = lireCoords(plateau) # Reprend les valeur des tours d'arrive et de depart a partir de la fonction precedente
    tdepart = plateau[x]
    tarrive = plateau[y]
    print("Je deplace le disque", disqueSup(plateau, x), "de la tour", x, "a la tour", y)
    tarrive.append(disqueSup(plateau, x)) # Modification de la configuration du plateau
    tdepart.remove(disqueSup(plateau, x))
    dessineConfig(plateau, n)
    return x


#print(jouerUncoup([[3,2,1], [], []], 3))


def boucleJeu(plateau, n): # Question 3
    cpt = 1
    max_coups = (2**n - 1) + 5*n # On ajoute une marge de 5*n au coup maximum autorise pour gagner
    annuler = "non"
    coups = {0 : copy.deepcopy(plateau)} 
    dessinePlateau(n)
    while verifVictoire(plateau, n) != True and max_coups > 0: # Continue de jouer tant que l'utilisateur n'a pas gagne et que le coups maximum n'est pas encore atteint
        print("Coup numero", cpt)
        disq = jouerUncoup(plateau, n)
        if cpt != 1: 
            effaceDisque((disqueSup(plateau, disq)), plateau, n)
        print(plateau)
        turtle.up()
        turtle.goto(-300, -200) # Se replace aux bonnes coordonnees
        turtle.down()
        coups[cpt] = copy.deepcopy(plateau) #l'utilisation du module copy permet de ne pas modifier toutes les valeurs du dictionnaire à chaque iteration de la boucle
        annuler = turtle.textinput("Annuler", "Voulez-vous annuler votre dernier coup ? ")
        if annuler.lower() == "oui" :
            x, y = annulerDernierCoup(coups)
            jouerUncoup(plateau, n, x, y)
            print("Coups annule, voici le plateau", plateau)
            effaceTout(plateau, n)
            turtle.up()
            turtle.goto(-300, -200)
            turtle.down()
            turtle.right(90)
        else :
            cpt += 1
            max_coups -= 1
    if verifVictoire(plateau, n) == True:
        print("Tu a gagne en", cpt-1, "coups.")
        nom = turtle.textinput("Nom", "Quel est votre nom ? ")
        scores = sauvScore(nom, n, cpt - 1)
        return scores #la fonction renvoit le dictionnaire scores avec les noms et scores de chacun en cas de victoire seulement
    else:
        print("Depassement du nombre maximum de coups autorises.")
        print("Tu a perdu apres", cpt-1, "coups.")
        solution = turtle.textinput("Solution", "Voulez-vous voir la solution ?")
        if solution.lower() == "oui":
            deplacement(solution, n)
#print(boucleJeu2([[3,2,1], [], []], 3))

#partie D

def dernierCoup(coups) :
    dernier = 0
    tour_depart = 0
    tour_arrivee = 0
    tours = [0, 1, 2]
    for cle in coups : #boucle pour trouver le dernier coup
        if cle > dernier :
            dernier = cle
    if coups[dernier - 1] != coups[dernier] :
        for i in range(len(coups[dernier])) : #boucle pour supprimer la tour qui ne peut etre ni celle de depart, ni celle d'arrivee (il y a forcement une tour qui ne bouge pas entre 2 coups)
            if coups[dernier - 1][i] == coups[dernier][i] :
                tours.pop(i)
    for y in tours : #grâce a la liste tours on ne cherche que dans les tours qui sont differentes d'un coup a l'autre
        if dernier >= 2 : #on differencie alors la tour de depart et la tour d'arrivee. On sait que la tour de depart doit posseder au moins un elements, tout comme la tour d'arrivee
            if len(coups[dernier - 1][y]) != 0 and len(coups[dernier - 1][y]) > len(coups[dernier][y]) : #la tour de depart a une longeur superieur a cette meme tour dans le coup suivant
                tour_depart = y                                                                          #car on lui enleve un element
            if len(coups[dernier][y]) != 0 and len(coups[dernier - 1][y]) < len(coups[dernier][y]) : #et inversement pour celle d'arrivee
                tour_arrivee = y
        else :
            tour_depart = 0 #s'il y a moins de 2 coups la tour de depart est forcement la 0
            if len(coups[dernier][y]) > 0 : #la tour d'arrivee est alors celle qui possede un element
                tour_arrivee = y              
    return tour_depart, tour_arrivee

def annulerDernierCoup(coups) :
    dernier = 0
    tour_arrivee, tour_depart = dernierCoup(coups) #on appelle la fonction dernierCoup pour inverser les tour d'arrivee et de depart
    for cle in coups : #on trouve le dernier coup comme dans la fonction dernierCoup pour ensuite le supprimer du dictionnaire coups
        if cle > dernier :
            dernier = cle
    del coups[dernier]
    return tour_depart, tour_arrivee #on renvoit les tours d'arrivee et de depart pour annuler le coup

#partie E

def sauvScore(nom, n, ncoups) :
    scores = {}
    if nom in scores : #condition si un meme joueur joue plusieurs parties
        scores[nom] += (n, ncoups)
    else : #condition pour un nouveau joueur
        scores[nom] = (n, ncoups)
    return scores #la fonction renvoit un dictionnaire avec les noms comme cles et un tuple pour les valeurs

def afficheScores(scores, n) :
    dico = {}
    classement = {}
    c = 1
    for cle in scores : #premiere boucle pour inverser les cles et les valeurs du dictionnaire scores afin de pouvoir classer par nombre de coups
            dico[scores[cle][1]] = cle
    for i in dico : #deuxieme boucle permettant d'ajouter les joueurs dans un dictionnaire classement par rapport à leur nombre de coups
         for y in dico :
            if i > y and dico[y] not in classement.values() :
                classement[c] = dico[y]
                c += 1
            elif i <= y and dico[y] not in classement.values() :
                 classement[c] = dico[y]   
    print("Voici le classement pour", n, "disques :")    
    for i in classement :
         print(i, classement[i]) #troisieme boucle pour faire un affichage de la forme d'un classement



# Partie F

def mouvement(n, i, j, k): # Question 1. Algorithme fait de maniere recursive prise sur Internet prenant en argumant le nombres de disques les 3 tours
    if n == 1:
        return [(i, k)]
    return mouvement(n - 1, i, k, j) + [(i, k)] + mouvement(n - 1, j, i, k)

#print(mouvement(3, 0, 1, 2))

#solution = mouvement(n, 0, 1, 2)

def deplacement(liste, n): # Question 2
    plateau = init(n)
    fin_a = solution[-1][0] # Prend la derniere valeur de la tour de depart 
    fin_b = solution[-1][1] # Prend la derniere valeur de la tour d'arrive
    while verifVictoire(plateau, n) != True:
        for i in range(len(solution) - 1): # Parcours la liste des mouvements a effectuer (solution)
            x = solution[i][0]
            y = solution[i][1]
            jouerUncoup(plateau, n, x, y) # Dessine la configuration du plateau d'apres la liste des mouvements a effectuer
            effaceTout(plateau, n)
            turtle.right(90)
        jouerUncoup(plateau, n, fin_a, fin_b) # Dessine la configuration finale du plateau pour eviter qu'elle ne soit efface dans la boucle
        
#print(deplacement(solution, 3))


# Principale principal

print("Bienvenue dans les tours de Hanoi")
jouer = "oui"
scores = {}
classement = {}
while jouer.lower() == "oui" :
    n = int(turtle.numinput("Disques", "Combien de disques ?",minval=1))
    plateau = init(n)
    solution = mouvement(n, 0, 1, 2)
    turtle.reset()
    scores = boucleJeu(plateau, n)
    if scores != None : #condition permettant de ne pas avoir d'erreur en cas de defaite car dans ce cas la ce dictionnaire sera vide
        for nom in scores : #boucle permettant d'ajouet au fur et à mesure les joueurs dans le dictionnaire classement car scores change a chaque iteration
            if nom not in classement :
                classement[nom] = scores[nom]
            else :
                classement[nom] += scores[nom]
    jouer = turtle.textinput("Rejouer", "Voulez vous continuer de jouer ? ")
afficheScores(classement, n)
print("Au revoir")
