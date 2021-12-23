#Noms: ALVAREZ Samuel Bibal Louis
#Projet informatique: Bataille Navale
#
#16 décembre 2021
#L2 MIASHS Panthéon Sorbonne
 
import random
import pygame

#Constantes projet
#dimension du plateau de jeu NxN
N=10
COLONNES=[str(i) for i in range(N)]
LIGNES = [' '] + list(map(chr, range(97, 107)))
DICT_LIGNES_INT = {LIGNES[i]:i-1 for i in range(len(LIGNES))}
#case pas attaquée
VIDE = '.'
#case attaquée sans bateau
EAU='o'
#case attaquée avec bateau
TOUCHE='x'
#présence d'un bateau
BATEAU='B'
#case attaquée et bateau coulé
DETRUIT='@'
#Nom des bateaux
NOMS=['Transporteur','Cuirasse','Croiseur','Sous-marin','Destructeur']
#Nombre de cases occupées respectivement au nom des bateaux
TAILLES=[5,4,3,3,2]
 
#init de pygame 
pygame.init()
eau_effect = pygame.mixer.Sound("D:\\L2 Python\\Bataille Navale\\Plouf_1.mp3")
touche_effect=  pygame.mixer.Sound("D:\\L2 Python\\Bataille Navale\\explosion_courte.mp3")
detruit_effect=  pygame.mixer.Sound("D:\\L2 Python\\Bataille Navale\\detruit.mp3")
victoire_effet = pygame.mixer.Sound("D:\\L2 Python\\Bataille Navale\\foule_joie.mp3")
 
def SoundManque():
    eau_effect.play()   # le son est joué

def SoundTouche():
    touche_effect.play()   # le son est joué
    
def SoundDetruit():
    detruit_effect.play()    # le son est joué
    
def SoundVictoire():
    victoire_effect.play()   #  le son est joué
    
#Fonctions Partie 1
 
#Partie 1.1
def create_grid():      
   return [[VIDE]*N for i in range(N)]
# Renvoi une matrice de taille N × N remplie avec le symbole VIDE.
 
#Partie 1.2
def plot_grid(m):
   print("\n  " + " ".join(COLONNES[x] for x in range(0, N)))
   # concatène les éléments de la liste COLONNES en commençant par un retour à la ligne et deux blancs
   # les éléments de COLONNES sont séparés (méthode join)
   if len(m) != 0:  #on contrôle que la liste n'est pas vide
                    # car sinon m[r] n'a plus aucun sens puisque m est vide
 
       for r in range(len(LIGNES)-1):  # -1 car dans les constantes LIGNES commence par un blanc
           print(LIGNES[r+1] + " " + " ".join(str(c) for c in m[r]))
           # r+1 en indice également car il y'a 11 éléments
   print()
# la fonction ne renvoie rien au final
 
 
#Partie 1.3
# première fonction de tir du projet
def tir_basique(m,pos):
    if len(pos) == 2 and len(m) != 0: 
#controle de la validite de pos [0] et pos [1] pour ne pas sortir de la grille m
        if pos [0] >=0 and pos [0] <= (N-1) and pos [1] >=0 and pos [1] <= (N-1):
#si la valeur de 'm' a la position pos est differente de EAU (c'est a dire VIDE pour la partie 1) alors c est un tir nouveau
            if m [pos[0]][pos[1]] != EAU:
               m [pos[0]][pos[1]] = EAU
               print ("Tir nouveau")
               SoundManque()
               return True
            else:
#sinon c'est un tir deja fait
               print ("Tir deja fait")
               return False
        else:
            print ("Tir hors cadre")
    else:
#ici pos est mal defini ou m est vide le tir est considere comme non valide
        print ("Tir invalide")
 
    return False
 
 
#Partie 1.4
def random_position ():
   letter = chr (random.randint(97, 97+N-1))
   # on tire au hasard un nombre entre 97 et 106
   # puis avec "chr" on le transforme en lettre via la table ascii
   # donc ici cela sera entre a et j
   nombre = random.randint(0,N-1)
   pos = letter+" "+str(nombre)
   return pos
 
 
#Partie 1.6
def pos_from_string(s):
#initialisation de pos en tant que tuple vide
    pos = tuple()  
   
    if len(s)==3:  #3 car on a une lettre un espace et un chiffre
        s=s.split()
        if len(s)==2 and s[0] in LIGNES and s[1] in COLONNES:
           Nombre = int(s[1])  #forçage de type car s[1] est un str or il doit etre un nombre
           Lettre = s[0]
           NLettre =int(ord(Lettre)) - 97 # on converti la lettre en chiffre via ord et la table ascii
           # puisque le code ascii de a est 97
           # la différence entre le code ascii de s[0] et 97 donnera le premier élément du tuple
           pos=(NLettre,Nombre)
        else:
           print ("Format invalide veuillez saisir une autre position: ",s)
           print ("Position: Ecrivez une lettre minuscule entre a et j, puis mettre un espace, puis ecrivez un chiffre entre 0 et 9")
 
    return pos
 
 
#FONCTION: Test_Partie_1
# Fonction Test qui permet de tester chaque fonctions de la partie 1
def Test_Partie_1():  
    print ("Debut tests partie 1\n")
    print ("Creation et representation de la grille\n")
    m=create_grid() 
    plot_grid(m)
    print ("Valeur retour de la fonction pos_from_string - pour la string -b 4-\n")
    print(pos_from_string("b 4"))
   
    print ("Test de la fonction tir\n")
    test=0
    while True :
        if test==5:
            break
       
        print ("Position: Ecrivez une lettre minuscule entre a et j, puis mettre un espace, puis ecrivez un chiffre entre 0 et 9")
        a=str(input("Choisir une position: "))
       
        pos=pos_from_string(a)
        b=tir_basique(m,pos)
       
        if b==False:
            print("Position déjà attaquée ou tir invalide")
      
        plot_grid(m)
        test+=1
 
    print ()
    input ("Appuyez sur n importe quelle touche pour continuer")
    nb_tirs = 10  # on va faire 10 tirs au hasard et on va regarder leur répartition sans erreur
    print ("On va faire ",nb_tirs," tirs random")
    test = 1
    while True:
        TirJoueur = random_position ()
        pos = pos_from_string (TirJoueur)
        tir_basique (m,pos)
        plot_grid(m)
        test +=1
       
        if test >nb_tirs:
            break
   
    print ("Fin test partie 1\n\n")
 
 
#Fonctions Parties 2
#Partie 2.1
def nouveau_bateau(flotte,nom,taille,pos,orientation):
   d={}
   d["nom"]=nom 
   d["taille"]=taille 
   d["cases touchées"]=0 
 # h va etre les lignes i.e les lettres de "a" à "j"
# v va être les colonnes i.e les chiffres de 0 à 9
   accept = True
   l=[]
   if orientation=="h":
#controle que la position de depart et finale du bateau tombent dans la grille
       if pos[1] in range(0,len(COLONNES)) and (pos[1]+taille-1) in range(0,len(COLONNES)):
#on controle qu'un bateau ne va pas en couper un autre on va donc controler que toutes les positions sont valides
            for i in range(pos[1],pos[1]+taille):  # i parcourt toutes les cases du bateau
                a=(pos[0],i)  #pos[0] ne bouge pas car le bateau est placé à l'horizontale
                if presence_bateau(a,flotte) == False:
                    l.append(a)
                else:
                    print("ERREUR ! Une des positions du bateau est commune avec un ou plusieurs autre bateaux")
                    accept =  False
       else:
           print("ERREUR ! La position initiale ou finale horizontale du bateau est hors grille:")
           accept =  False         
   if orientation=="v": 
       #controle que la position de depart et finale du bateau tombent dans la grille
       if pos[0] in range(0,len(LIGNES)-1) and (pos[0]+taille-1) in range(0,len(LIGNES)-1):
           for j in range(pos[0],pos[0]+taille):
                b=(j,pos[1])
                if presence_bateau(b,flotte) == False:
                    l.append(b)
                else:
                    print("ERREUR ! Une des positions du bateau est commune avec un ou plusieurs autre bateaux")
                    accept =  False
       else:
           print("ERREUR ! La position initiale ou finale verticale du bateau est hors grille:")
           accept =  False
 
   if accept:  #si durant tous les test accept n'a pas pris la valeur False alors on peut ajouter le bateau
       d["positions"]=l  #on affecte à la clé "positions" la liste l
       flotte.append(d)
       return True
   else:
       return False
 
#Partie 2.2
#flotte est une liste de dictionnaires et chaque dictionnaire représente un bateau
def presence_bateau(pos,flotte):
#ici, bateau parcours tous les dictionnaires de flotte
   for bateau in flotte:
#ici, inpos va parcourir les valeurs des clés "position" de chaque bateau
       for inpos in bateau["positions"]:
        if pos[0] == inpos [0] and pos[1] == inpos [1]:  #on regarde si la position est occupée
           return True
   return False
 
 
#Partie 2.3
def plot_flotte_grid(m,flotte):
    #ici on parcourt la matrice m et si un bateau est sur une position
    #On met BATEAU sur les positions qu'il occupe
   for x in range(len(m)):
       for y in range(len(m[x])):
           if presence_bateau((x,y),flotte) == True:
               m[x][y]=BATEAU
   plot_grid(m)
 
#Partie 2.4
def input_ajout_bateau(flotte,nom,taille):
   from re import match
   re=r"^[a-j] [0-9]$"
   while True:
       s=str(input("Position: Ecrivez une lettre minuscule entre a et j, puis mettre un espace, puis ecrivez un chiffre entre 0 et 9: "))
       while not match(re,s):  #test si la position a le bon format via la méthode match de la librairie re
           s=str(input("ERREUR: Ecrivez une lettre minuscule entre a et j, puis mettre un espace, puis ecrivez un chiffre entre 0 et 9: "))
       pos=pos_from_string(s)
#la variable orientation est initialisee avec n 'importe quelle valeur qui n'est ni h ni v    
       orientation="a"
       while orientation!="h" and orientation!="v":  #test de validité de l'orientation
           orientation=str(input("Orientation : Horizontale (tapez h) ou Verticale (tapez v): "))
       if len(flotte) > 0:
           if presence_bateau(pos,flotte)==True:  #test de présence
               print("ERREUR ! Un bateau est déjà sur cette position, donnez une nouvelle position pour ce bateau")
           else: 
               if nouveau_bateau(flotte,nom,taille,pos,orientation)==True:
                   break
       else:
           if nouveau_bateau(flotte,nom,taille,pos,orientation)==True:
               break
#si la flotte est vide on ajoute directement le bateau via un appel de nouveau_bateau
#puisque nouveau_bateau retourne True c'est que le bateau a été ajouté
#alors on teste si nouveau_bateau a bien fonctionné
 

#Partie 2.5
def input_ajout_bateau_ia(flotte,nom,taille):
   print ("Ajout du bateau ", nom," taille ", taille)
   while True:
#generation au hasard d un couple de position (letttre nombre)
       randomstr = random_position ()
       pos=pos_from_string(randomstr)
#on fait une sorte de loi de Bernoulli pour que l'ia chosisse une orientation au hasard
       randomorient = random.randint (0,1)
       if randomorient == 0:
           orientation = "h"
       else:
           orientation = "v"
#s'il y a deja des bateaux alors des contrôles vont se faire
#contrôle que le bateau est entierement dans la grille avec nouveau_bateau
#contrôle que le bateau ne coupe pas un bateau deja dans la flotte avec nouveau_bateau
       if len(flotte) > 0:
           if presence_bateau(pos,flotte)==False and nouveau_bateau(flotte,nom,taille,pos,orientation)==True:
               break
#c est le premier bateau on appel nouveau_bateau
       else:
           print ("bateau",nom," ajoute ","positions ",pos,"\n")
           if nouveau_bateau(flotte,nom,taille,pos,orientation)==True:
               break
 

#Partie 2.6
def init_joueur():
   flotte=[]
#avec la boucle for on demande à l'utilisateur de rentrer les 5 bateaux
   for i in range(5):
        nomdubateau = NOMS[i]
        tailledubateau = TAILLES[i]
        print ("Placez le bateau: ",nomdubateau)
        input_ajout_bateau(flotte,nomdubateau,tailledubateau)
 
   return flotte


#Partie 2.7
def init_joueur_ia():
   flotteia=[]
#la boucle va ajouter les 5 bateaux definis de façon aléatoire pour l'ia
   for i in range(5):
        nomdubateau = NOMS[i]
        tailledubateau = TAILLES[i]
        input_ajout_bateau_ia(flotteia,nomdubateau,tailledubateau)
 
   return flotteia


#Fonctions Partie 3
#Partie 3.1
def tir (pos,m,flotte):
    tirstatus = False
# pos doit etre de longueur egale a 2 il doit y avoir des bateaux dans la flotte et la grille ne doit pas etre vide
    if len(pos) == 2 and len(flotte) > 0 and len(m) > 0:
#si pas egal a EAU ou TOUCHE ou DETRUIT tir deja fait
        if m [pos[0]][pos[1]] == EAU or m [pos[0]][pos[1]] == TOUCHE or m [pos[0]][pos[1]] == DETRUIT:
            print ("Tir deja fait")
            tirstatus = False
#si egal a VIDE nouveau tir mais manqué on change la valeur de la case en EAU
        elif m [pos[0]][pos[1]] == VIDE:
            print ("MANQUE !")
            m [pos[0]][pos[1]] = EAU
            tirstatus = True
            SoundManque()
        elif m [pos[0]][pos[1]] == BATEAU and presence_bateau(pos,flotte) == True:
            print ("TOUCHE !")
            m [pos[0]][pos[1]] = TOUCHE
            SoundTouche()
#on recherche le rang du  bateau grace à la fonction id_bateau...
            index = id_bateau_at_pos(pos,flotte)
            tirstatus = True  #le tir a été effectué
#on contrôle que le rang du bateau retourné est valide
            if index is not None:
            #on incremente la valeur de la clé "cases touchées"
            #case touchées est au final comme la jauge de vie du bateau
               flotte [index]["cases touchées"] = flotte [index]["cases touchées"] + 1
               if flotte [index]["cases touchées"] == flotte [index]["taille"]:
            #si à la suite du tir la valeur de "cases touchées" est égale à la taille
            #cela signifit que le bateau a été détruit
                   print ("Bateau ----->",flotte [index]["nom"],"COULE !")
                   for inpos in flotte [index]["positions"]:
                       #controle de la validite de inpos [0] et inpos [1] pour ne pas sortir de m
                       if inpos [0] >=0 and inpos [0] <= (N-1) and inpos [1] >=0 and inpos [1] <= (N-1):
                           m[inpos [0]][inpos [1]]=DETRUIT  #on remplace le bateau par DETRUIT
                           SoundDetruit()
            #on retire le bateau de la flotte
#on verra par la suite que si on a retiré tous les bateaux de la flotte i.e len(flotte)==0
#alors la partie est finis car l'une des flottes a été totalement détruite
                   flotte.pop(index)
    else:
        print ("Tir invalide")
        tirstatus = False
 
#on retourne le status du tir True si il a été fait False sinon
    return tirstatus


#Partie 3.2
def id_bateau_at_pos(pos,flotte):
#on passe en revue toute les positions de chaque bateau avec inpos
#si aucune correspondance n'est trouvée on incrémente rang de +1
#En revanche si on trouve une position d'un bateau qui est la même que celle donnée en argument
#on retourne la varianble rang qui est le rang du bateau dans la liste flotte
   rang = 0
   for bateau in flotte:
       for inpos in bateau["positions"]:
            if pos[0] == inpos [0] and pos[1] == inpos [1]:
               return rang
       rang = rang + 1
   return None


#FONCTION: Test_Partie_2_et3
def Test_Partie_2_et3():
    print ("Debut tests parties 2 et 3\n")
    grille1 =[]
    grille1=create_grid()
    print ("Grille initiale")
    plot_grid(grille1)
    print("Resultat de la fonction pos_from_string pour la posotion b 4\n", pos_from_string("b 4"))
#on cree une nouvelle flotte
    flotte=[]
#test bateau dont la position initiale depasse la grille verticalement
    print("Bateau place hors grille verticalement")
    print("Resultat de la function nouveau_bateau: ",nouveau_bateau(flotte,"Test",3,(10,0),'v'))
#bateau n'est pas ajoute a la flotte
    print("Le bateau n a pas ete ajoute a la flotte et la grille est vide")
    print (flotte)
    plot_flotte_grid(grille1,flotte)
#test bateau dont la position initiale dépasse la grille hoorizontalement
    print("Bateau place hors grille horizontalement")
    print("Resultat de la function nouveau_bateau: ",nouveau_bateau(flotte,"Test",3,(0,10),'h'))
#bateau n'est pas ajouté a la flotte
    print("Le bateau n a pas ete ajoute a la flotte et la grille est vide")
    print (flotte)
    plot_flotte_grid(grille1,flotte)
#on test un bateau avec une bonne position initiale mais qui depasse horizontalement
    print("Bateau qui depasse de la grille grille horizontalement")
    print("Resultat de la function nouveau_bateau: ",nouveau_bateau(flotte,"Test",3,(0,8),'h'))
    print("Le bateau n a pas ete ajoute a la flotte et la grille est vide")
    print (flotte)
    plot_flotte_grid(grille1,flotte)
    print ("Placement de trois bateaux aux positions:\n 5;0 H taille 3\n 0;0 H taille 3\n 5;4 V taille 3\n")
    print("Resultat de la function nouveau_bateau pour le premier bateau: ",nouveau_bateau(flotte,"Test",3,(5,0),'h'))
    print("Resultat de la function nouveau_bateau pour le deuxieme bateau: ",nouveau_bateau(flotte,"Vogues Merry",3,(0,0),"h"))
    print("Resultat de la function nouveau_bateau pour le troisieme bateau: ",nouveau_bateau(flotte,"Daron",3,(5,4),"v"))
    print("Les bateaux ont ete ajoutes a la flotte et la grille n est pas vide")
    print (flotte)
    plot_flotte_grid(grille1,flotte)
    print ("Test de la presence d un bateau sur la position 0;1\n")
    pos=(0,1)
    if presence_bateau((0,1),flotte):
        print ("Un bateau est place sur la position: ", pos,"\n")
    else:
        print ("Pas de bateau sur la position: ",pos,"\n")
    input("\nTapez n'importe qu'elle touche pour continuer")
#on créé une nouvelle flotte et le joueur va placer les bateaux et faire quelques tirs
    grille2=create_grid()
    plot_grid(grille2)
    print("Vous allez placer votre flotte\n")
    flotte = init_joueur()
    print("Ceci est la flotte entree\n")
    print (flotte)
    print("\nCeci est son placement sur la grille")
    plot_flotte_grid(grille2,flotte)
    nbtir = 10
    print ("Test de la fonction tir - ",nbtir,"tirs peuvent etre fait\n")
    test=0
    while True:
        if test==nbtir:
            break
        print ("Position: Ecrivez une lettre minuscule entre a et j, puis mettre un espace, puis ecrivez un chiffre entre 0 et 9")
        a=str(input("Choisir une position: "))
        pos=pos_from_string(a)
        b=tir(pos,grille2,flotte)
        if b==False:
            print("Position déjà attaquée ou tir invalide")
        plot_grid(grille2)
        test+=1
#on créé une nouvelle flotte et l'ia va placer automatiquement les bateaux
#puis déclencher un nombre de tirs qui sera demandé
    print ("\nIA va placer automatiquement les bateaux\n")
    input("Tapez n'importe qu'elle touche pour continuer")
 
    grille3=create_grid()
    plot_grid(grille3)
    flotte_ia = init_joueur_ia()
    print ("Flotte IA et grille de depart\n")
    print (flotte_ia)
    plot_flotte_grid(grille3,flotte_ia)
#on demande à l'utilisateur de rentrer un nombre sous forme de chaine et on contrôle que cette chaine
#represente bien un nombre sinon on redemande
    while True:
        tirinput = str(input ("\nEntrer le nombre de tirs au hasard a declencher : "))
        if tirinput.isdigit():
            tirmax = int(tirinput)
            break
    go = 0
    while True:
        go +=1
        if go < tirmax:
           s = random_position ()
           pos=pos_from_string(s)
           tir (pos,grille3,flotte_ia)
           plot_grid (grille3)
        else:
           break
   
    print ("Grille finale")
    plot_grid (grille3)
    print ("Flotte finale")
    print (flotte_ia)
    print ("\nFin tests parties 2 et 3\n")
 
 
#Fonctions Partie 4
#Partie 4.1
def tour_ia_random(m,flotte):
    if len(flotte) >0:
        while True:
            s = random_position ()
            pos=pos_from_string(s)
#Si le symbole VIDE ou BATEAU est trouvé alors la position n'a pas encore ete touche et on tir
            if m [pos[0]][pos[1]] == VIDE or m [pos[0]][pos[1]] == BATEAU:
                tir (pos,m,flotte)
                break

#Partie 4.2
#différence avec la partie 4.1 est qu'ici l'IA peut se tromper et faire des tirs déjà faits
def tour_ia(m,flotte):
    if len(flotte) >0:
        s = random_position ()
        pos=pos_from_string(s)
        tir (pos,m,flotte)


#Partie 4.3
def tour_joueur(nom,m,flotte):
    from re import match
    re=r"^[a-j] [0-9]$"
#on demande une position de tir et on vérifie la syntaxe
    while True:
        s=str(input("Position: Ecrivez une lettre minuscule entre a et j, puis mettre un espace, puis ecrivez un chiffre entre 0 et 9: "))
       
        while not match(re,s):
            s=str(input("ERREUR: Ecrivez une lettre minuscule entre a et j, puis mettre un espace, puis ecrivez un chiffre entre 0 et 9: "))
        pos=pos_from_string(s)
#on vérifie ensuite si le tir a déjà été fait ou non       
        if m [pos[0]][pos[1]] == VIDE or m [pos[0]][pos[1]] == BATEAU:
            tir (pos,m,flotte)
            break
        else:
            print ("Joueur: ", nom," - tir deja fait ou invalide recommencez s il vous plait")
 
 
#Partie 4.4
#regarde s’il y a un bateau touch́e et non detruit dans m.
#S’il y en a un, il tire sur une case adjacente qui n’a pas encore  ete attaqúee, sinon il tire au hasard.
def tour_ia_better_random(m,flotte):
    bateautrouve = False
    for x in range(len(m)):
       for y in range(len(m[x])):
           if m[x][y]==TOUCHE:
                bateautrouve = True
                pos = (x,y)
                break
 
# si bateautrouve est egal a True alors on a trouvé un bateau
    if bateautrouve == True:
        print (pos)
#adjacent liste de coordonnées des cases adjacentes autour de x,y
# x-1,y; x+1,y; x,y-1; x,y+1; x-1,y+1; x-1,y-1; x+1,y+1 ;x+1,y-1
        adjacent=  [(pos[0],pos[1]),(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]-1),(pos[0],pos[1]+1),(pos[0]-1,pos[1]+1),(pos[0]-1,pos[1]-1),(pos[0]+1,pos[1]+1),(pos[0]+1,pos[1]-1)]
        print (adjacent)
        for i in adjacent:
            if i[0] in range(0,len(LIGNES)-1) and i[1] in range(0,len(COLONNES)):
#on tire que sur les cases qui n ont pas ete touchées
                if m [i[0]][i[1]] == VIDE or m [i[0]][i[1]] == BATEAU:
                    tir (i,m,flotte)
                    break
#si on trouve pas de bateau
    else:
           s = random_position ()
           pos=pos_from_string(s)
           tir (pos,m,flotte)


#Partie 4.5
def test_fin_partie(nom,m,flotte,nb_tir):   
    if len(flotte) == 0:  #si la flotte est vide c'est que la partie est finie
        print("Nom du vainqueur: ",nom," victoire obtenue en :",nb_tir," tirs")
        print ("Grille finale")
        plot_grid (m)
        print (flotte)
        SoundVictoire()
        exit ()


#Partie 4.6
def hide():
    print("\n" * 200)
#on imprime juste 200 lignes blanches
 
 
#Partie 4.7
#ne precise pas les positions des bateaux sur la grille
#utile pour un jeu a plusieurs ou les bateaux doivent etre caches
#rend le jeu plus intéressant car on ne voit pas les bateaux de l'adversaire
def plot_grid_hide_bateau (m):
    print("\n  " +  " ".join(COLONNES[x] for x in range(0, N)))    
    for x in range(len(m)):
        txt =""
        for y in range(len(m[x])):
            if m[x][y]==BATEAU:
                txt += " "+VIDE  #lorsque on a bateau on met vide à la place pour cacher le bateau sur la grille
            else:
                txt += " "+m[x][y]
        
        print(LIGNES[x+1] +  txt)
       
    print()


#Partie 4.8
def joueur_vs_ia():
#initialisation
#Le joueur joue sur la grille de l 'ia
#l'ia joue sur la grille du joueur
    flotteia=init_joueur_ia()
    gridia=create_grid()
    plot_flotte_grid(gridia,flotteia)
    hide()
    print ("grille et flotte ia initialisees\n")
    nomjoueur=str(input("entrez votre nom\n"))
    flottejoueur = init_joueur()
    griduser=create_grid()
    plot_flotte_grid(griduser,flottejoueur)
    print ("grille et flotte de:",nomjoueur," initialisées\n")
    nb_tir_user =0
    nb_tir_ia =0
   
    while True:
        print("Tour de:",nomjoueur," \n")
        print ("Grille ia avant tir")
        plot_grid_hide_bateau(gridia)
        tour_joueur(nomjoueur,gridia,flotteia)  #le joueur tir sur la grille et la flotte de l'ia
        print ("Grille ia apres tir")
        plot_grid_hide_bateau(gridia)
#on incrémente les compteur de jeu
        nb_tir_user =nb_tir_user + 1
#on test si un des joueurs a coulé la flotte de son adversaire avec la fonction test_fin_partie
        test_fin_partie(nomjoueur,gridia,flotteia,nb_tir_user)   
        input("Tour de l'ia \n Selectionnez n importe qu elle touche pour faire jouer l'ia")
        hide()  #on imprime 200 lignes blanches et on passe au tour de l'Ia
        print ("Grille de",nomjoueur," avant tir \n")
        plot_grid_hide_bateau(griduser)
        tour_ia (griduser,flottejoueur)
        print ("Grille de:",nomjoueur," apres  tir \n")
        plot_grid_hide_bateau(griduser)
        nb_tir_ia =nb_tir_ia + 1
        test_fin_partie("ia",griduser,flottejoueur,nb_tir_ia)
        input("Entrez n importe quelle touche")
        hide()
#c'est le exit de la fonction test_fin_partie qui va pouvoir arrêter la boucle en cas de victoire de l'Ia ou du joueur
 
#Partie 4.9
def joueur_vs_joueur():
    print ("Tour Joueur 1")
    nomjoueur1=str(input("entrez votre nom \n"))
    flotte1=init_joueur()
    grid1=create_grid()
    plot_flotte_grid(grid1,flotte1)
    print (nomjoueur1," grille et flotte initialisees - selectionnez n importe quelle touche pour continuer\n")
    hide()
    print ("Tour Joueur 2")
    nomjoueur2=str(input("entrez votre nom \n"))
    flotte2 = init_joueur()
    grid2=create_grid()
    plot_flotte_grid(grid2,flotte2)
    print (nomjoueur2," grille et flotte initialisees - selectionnez n importe quelle touche pour continuer\n")
    hide()
    nb_tir_user1 =0
    nb_tir_user2 =0
    while True:
        print("Tour de:",nomjoueur1,"\n")
        print ("Grille de:",nomjoueur2," avant tir\n")
        plot_grid_hide_bateau(grid2)
        tour_joueur(nomjoueur1,grid2,flotte2)
        print ("Grille de:",nomjoueur2," apres tir\n")
        plot_grid_hide_bateau(grid2)
        nb_tir_user1 =nb_tir_user1 + 1
        test_fin_partie(nomjoueur1,grid2,flotte2,nb_tir_user1)
        input("Entrez n importe quelle touche")
        hide()
        print("Tour de:",nomjoueur2," \n")
        print ("Grille de:",nomjoueur1," avant tir\n")
        plot_grid_hide_bateau(grid1)
        tour_joueur (nomjoueur2,grid1,flotte1)
        print ("Grille de",nomjoueur1," apres tir\n")
        plot_grid_hide_bateau(grid1)
        nb_tir_user2 =nb_tir_user2 + 1
        test_fin_partie(nomjoueur2,grid1,flotte1,nb_tir_user2)
        input("Entrez n'importe quelle touche")
        hide()


#Partie 4.10
def choix_joueur():
    while True:
        print("Choisissez votre mode de jeu:\n")
        print(" 0- si vous voulez jouer en solo \n")
        print(" 1- si vous voulez jouer à deux \n")
        print(" -1- pour quitter le menu \n")
        schoix1 = int(input("saisissez votre choix: "))
        if schoix1==0:
            joueur_vs_ia()
        elif schoix1==1:
            joueur_vs_joueur()
        elif schoix1==-1:
            break
        else:
            print("mauvais choix veuillez recommencer: \n")


#FONCTION: Test_Partie_4a
def Test_Partie_4a():
    print ("Debut tests partie 4a\n")
    print ("Test de la fonction tour_ia_random\n")
    nom = "IA"
    grille4=create_grid()
    plot_grid(grille4)
    flotte_ia = init_joueur_ia()
    print (flotte_ia)
    plot_flotte_grid(grille4,flotte_ia)
    gotir = int(input("Entrez le nombre de tirs maximum a faire: "))
    nb_tir =0
    while True:
        nb_tir +=1
        if nb_tir < gotir:
            print
            tour_ia_random(grille4,flotte_ia)
            test_fin_partie(nom,grille4,flotte_ia,nb_tir)
            print ("Nombre de tirs: ",nb_tir)
            print ("Bateaux visibles")
            plot_grid (grille4)
            print ("Bateaux caches")
            plot_grid_hide_bateau(grille4)
            print (flotte_ia)
        else:
            print ("\nNombre maximum de tirs atteint sans couler toute la flotte\n")
            print ("Nombre de bateaux restant: ",len(flotte_ia))
            break
    print ("Fin tests partie 4a\n")


#FONCTION: Test_Partie_4b
def Test_Partie_4b():
    print ("Debut tests partie 4a\n")
    print ("Test de la fonction tour_ia_better_random\n")
    nom = "IA"
    grille4=create_grid()
    plot_grid(grille4)
    flotte_ia = init_joueur_ia()
    print (flotte_ia)
    plot_flotte_grid(grille4,flotte_ia)
    nb_tour =0
    while True:
        nb_tour +=1
        if nb_tour < 200:
            tour_ia_better_random(grille4,flotte_ia)
            test_fin_partie(nom,grille4,flotte_ia,nb_tour)
            plot_grid (grille4)                                            
        else:
           break
    print ("Fin tests parties 4a\n")
 
 
def Test_Partie_4():
    #on créé un menu a l'intérieur de la fonction test pour demander à l'utilisateur
    #quelle fonction de la partie 4 il veut tester
    print ("Choisissez la partie que vous voulez tester:\n")
    print ("    0 - Test la fonction tour_ia_random\n")
    print ("    1 - Test la fonction tour_ia_better_random\n")
    print ("    2 - Choisir une partie\n")
    print ("\n un autre choix quitte le programme\n")
    schoix = str(input("saisissez votre choix: "))
    if schoix.isdigit():
        choix = int(schoix)
        if choix == 0:
            Test_Partie_4a()
        elif choix == 1:
            Test_Partie_4b()           
        elif choix == 2:
            choix_joueur()
        else:
            print ("Fin du choix")
            exit()
       
    else:
        print ("choix non valide recommencez\n")
 
 
#Fonctions PARTIE 5
#Partie 5.1   
def tour_boulet_de_canon(pos,m,flotte):
#case adjacente autour de x,y sont definies par les coordonnees suivantes
# x-1,y; x+1,y; x,y-1 ;x,y+1; x-1,y+1; x-1,y-1; x+1,y+1; x+1,y-1
        adjacent=  [(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]-1),(pos[0],pos[1]+1),(pos[0]-1,pos[1]+1),(pos[0]-1,pos[1]-1),(pos[0]+1,pos[1]+1),(pos[0]+1,pos[1]-1)]
        for adj in adjacent:
            if adj[0] in range(0,len(LIGNES)-1) and adj[1] in range(0,len(COLONNES)):   
                tir (adj,m,flotte)
 
   
#Partie 5.2
def tour_ia_even_better_random(m,flotte):
#regarde s il y a un bateau touché et non détruit dans m
    bateautrouve = False
    for x in range(len(m)):
       for y in range(len(m[x])):
           if m[x][y]==TOUCHE:
                bateautrouve = True
                pos = (x,y)
                break
           
    if bateautrouve:
        print (pos)
        adjacent=  [(pos[0],pos[1]),(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]-1),(pos[0],pos[1]+1),(pos[0]-1,pos[1]+1),(pos[0]-1,pos[1]-1),(pos[0]+1,pos[1]+1),(pos[0]+1,pos[1]-1)]
        print (adjacent)
        for adj in adjacent:
            if adj[0] in range(0,len(LIGNES)-1) and adj[1] in range(0,len(COLONNES)):   
                if m [adj[0]][adj[1]] == VIDE or m [adj[0]][adj[1]] == BATEAU:
                    tir (adj,m,flotte)
    else:
#tir au hasard
           s = random_position ()
           pos=pos_from_string(s)
           tir (pos,m,flotte)
          
 
#Partie 5.3
def presence_bateau_avec_case_adjacente(pos,flotte):
#construction de la liste des positions adjacentes a la position pos
#cette liste inclue la position pos, cette liste a 9 éléments.
    adjacent=  [(pos[0],pos[1]),(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]-1),(pos[0],pos[1]+1),(pos[0]-1,pos[1]+1),(pos[0]-1,pos[1]-1),(pos[0]+1,pos[1]+1),(pos[0]+1,pos[1]-1)]
    print (adjacent)
    for bateau in flotte:
        for batpos in bateau["positions"]:
            #alors on regarde si sur une case adjacente a pos il n y a pas de bateau
#boucle sur la liste des positions adjacente et verification avec une des positions occupees par le bateau
            for adjpos in adjacent:
                if adjpos[0] in range(0,len(LIGNES)-1) and adjpos[1] in range(0,len(COLONNES)):   
                    if adjpos[0] == batpos[0] and adjpos[1] == batpos[1]:
                        return True
 
    return False


#FONCTION: Test_Partie_5_boulet_de_canon
def Test_Partie_5_boulet_de_canon():
    print ("Debut tests partie 5\n")
    print ("Test de la fonction boulet de canonn")
    nom = "IA"
    grille4=create_grid()
    plot_grid(grille4)
    flotte_ia = init_joueur_ia()
    print (flotte_ia)
    plot_flotte_grid(grille4,flotte_ia)
    nb_tour =0
    bouletlance = False
   
    while True:
        nb_tour +=1
# nombre de coups total max 200
# une fois et une seule dans la partie le boulet de canon est lance
# pour ici il sera lance au hasard pour cela on tire un chiffre au hasard entre 0 et 10
# et si c'est égale a 5 et qu'il  a  pas été lancé on le lance sinon on utilise
# la fonction tour_ia_better_random
       
        if nb_tour < 200:
            s = random.randint (0,10)
            if bouletlance == False and s == 5:
                print ("tour_boulet_de_canon")
                s = random_position ()
                pos=pos_from_string(s)
                tour_boulet_de_canon(pos,grille4,flotte_ia)
                bouletlance = True
            else: 
                print ("tour_ia_random")
                tour_ia_random(grille4,flotte_ia)
            test_fin_partie(nom,grille4,flotte_ia,nb_tour)
            plot_grid (grille4)                                                     
        else:
           break
       
        input ("appuyez sur n 'importe quelle touche pour voir le coup suivant")
   
    print ("Fin tests partie 5\n")   
 
#FONCTION: Test_Partie_5_better_random
def Test_Partie_5_better_random():
    print ("Debut tests parties 5\n")
    print ("Test de la fonction boulet de canonn")
    nom = "IA"
    grille4=create_grid()
    plot_grid(grille4)
    flotte_ia = init_joueur_ia()
    print (flotte_ia)
    plot_flotte_grid(grille4,flotte_ia)
    nb_tour =0
#bouletlance test si le boulet a ete lancé au debut c'est False une fois lancée la valeur devient True
    bouletlance = False
   
    while True:
        nb_tour +=1
        if nb_tour < 200:
            s = random.randint (0,10)
            if bouletlance == False and s == 5:
                print ("tour_boulet_de_canon")
                s = random_position ()
                pos=pos_from_string(s)
                tour_ia_better_random(grille4,flotte_ia)
                bouletlance = True
            else: 
                print ("tour_ia_better_random")
                tour_ia_random(grille4,flotte_ia) 
            test_fin_partie(nom,grille4,flotte_ia,nb_tour)
            plot_grid (grille4)                                                     
        else:
           break
       
        input ("appuyez sur n 'importe quelle touche pour voir le coup suivant")
   
    print ("Fin tests partie 5\n")
 


#FONCTION: Test_Partie_5_position_adjacente
def Test_Partie_5_position_adjacente():
    from re import match
    re=r"^[a-j] [0-9]$"
#on cree une nouvelle flotte
    flotte=[]
#on ajoute un bateau
    nouveau_bateau(flotte,"Gon",3,(5,4),"v")
    nouveau_bateau(flotte,"Killua",3,(5,0),'h')
    nouveau_bateau(flotte,"Kurapika",3,(0,0),"h")
    print ("flotte:\n",flotte)
    grille=create_grid()
    plot_flotte_grid(grille,flotte)
   
    while True:
        s=str(input("Position: une lettre minuscule entre a et j suivi d'un espace, puis un chiffre entre 0 et 9 ('q' pour sortir): "))
        if s.upper() != "Q":  #si on décide de continuer
            while not match(re,s):
                s=str(input("ERREUR: Ecrivez une lettre minuscule entre a et j, puis mettre un espace, puis ecrivez un chiffre entre 0 et 9: "))
            pos=pos_from_string(s)
            if presence_bateau_avec_case_adjacente(pos,flotte):
                print("\nUn bateau est present sur la position ou une position adjacent\n")
            else:
                print ("\nPas de bateau sur la position ou une position adjacente\n")
        else:
            break
       
    
#FONCTION: Test_Partie_5
def Test_Partie_5():
    print ("Choisissez la partie que vous voulez tester:\n")
    print ("    0 - Test la fonction boulet de canon\n")
    print ("    1 - Test la fonction tour_ia_even_better_random (combinaison boulet de canon et random)\n")
    print ("    2 - Test de la presence bateau sur position adjacente\n")
    print ("\n un autre choix quitte le programme\n")
    schoix = str(input("saisissez votre choix: "))
    if schoix.isdigit():
        choix = int(schoix)
        if choix == 0:
            Test_Partie_5_boulet_de_canon()
        elif choix == 1:
            Test_Partie_5_better_random()
        elif choix == 2:
            Test_Partie_5_position_adjacente()
        else:
            print ("Fin du choix")
            exit() 
    else:
        print ("choix non valide recommencez\n")
 
 
#Menu du programme demande à l'utilisateur quelle partie du projet il veut tester
while True:
    print ("Choisissez la partie que vous voulez tester:\n")
    print ("    0 - Function de la partie 1\n")
    print ("    1 - Function de la partie 2 et 3\n")
    print ("    2 - Function de la partie 4\n")
    print ("    3 - Function de la partie 5\n")
    print ("\n un autre choix quitte le programme\n")
    schoix = str(input("saisissez votre choix: "))
    if schoix.isdigit():
        choix = int(schoix)
        if choix == 0:
            Test_Partie_1()
        elif choix == 1:
            Test_Partie_2_et3()
        elif choix == 2:
            Test_Partie_4()
        elif choix == 3:
            Test_Partie_5()
        else:
            print ("Fin du programme")
            exit() 
    else:
        print ("choix non valide recommencez\n")
